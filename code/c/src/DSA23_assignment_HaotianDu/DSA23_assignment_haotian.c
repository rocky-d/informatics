#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


#define LINE_BUFFER_SIZE 20000
#define MIN_WORD_LENGTH 1
#define MAX_WORD_LENGTH 200
#define WORD_TABLE_SIZE 800000
#define MAX_DIFFERENT_WORDS 100000
#define MAX_FREQUENT_WORDS 100
#define H_SIZE_INCREMENT 32  // for CountingArray.h in counting_sort_mf_words()


typedef unsigned int CountingInt;
typedef unsigned long HashInt;

typedef enum {
    NO_EXCEPTION,  // = 0
    MEMORY_ALLOCATION_EXCEPTION,  // = 1
    MEMORY_RELEASE_EXCEPTION,  // = 2
    FILE_OPENING_EXCEPTION,  // = 3
    WORD_SET_FULL_EXCEPTION  // = 4
} Exception;

typedef struct {  // stores a word and its occurrence times
    char word[MAX_WORD_LENGTH];
    CountingInt times;
} Word;

typedef struct {  // stores all Words, their hash values, and other information
    Word **w_table;  // w_table = word_table
    HashInt *hashes;
    CountingInt length;  // number of different words
    CountingInt total;  // number of all words
} WordSet;


// auxiliary functions
void throw(Exception e);  // e = exception
void clear_buffer(void);
void free_pointer(void *pointer);
HashInt hash_word(char *word);
HashInt probing_hash(HashInt hash, CountingInt pb);  // pb = probing

// major functions
WordSet *new_wordset(void);
void ask_filename(char *filename);
void read_file(WordSet *set, char *filename);
void counting_sort_mf_words(WordSet *set, Word *mf_words, int mf_len);  // mf = most_frequent
void fee_wordset(WordSet *set);


CountingInt total_collision = 0;
CountingInt longest_probing = 0;


int main(void) {
    char filename[MAX_WORD_LENGTH];
    WordSet *w_set = new_wordset();  // w_set = word_set
    Word mf_words[MAX_FREQUENT_WORDS];
    clock_t t0, t1, t2;  // timestamp 0, timestamp 1, timestamp 2

    printf("------------------------------------------\n");
    ask_filename(filename);  // step 1: ask the filename from user
    printf("Counting ...\n");

    t0 = clock();
    read_file(w_set, filename);  // step 2: store words
    t1 = clock();
    counting_sort_mf_words(w_set, mf_words, MAX_FREQUENT_WORDS);  // step 3: sort the most frequent words
    t2 = clock();

    // step 4: print the results
    printf("\n");
    printf("        The Most Frequent Words\n");
    printf("=======================================\n");
    printf("    No.   Word   Times   Permillage\n");
    printf("=======================================\n");
    for (int i = 0; i < MAX_FREQUENT_WORDS; ++ i) {
        printf("%6d.   %s\n", i + 1, mf_words[i].word);
        printf("%22d%11.3lf \u2030\n", mf_words[i].times, 1000 * (double)mf_words[i].times / w_set->total);
        printf("=======================================\n");
    }
    printf("\n");
    printf("               Word  Set\n");
    printf("      ===========================\n");
    printf("            Length:%8d\n", w_set->length);
    printf("            Total:%9d\n", w_set->total);
    printf("      ===========================\n");
    printf("       Fill rate:%13.3lf %%\n", 100 * (double)w_set->length / WORD_TABLE_SIZE);
    printf("       Longest probing:%9d\n", longest_probing);
    printf("       Total collision:%9d\n", total_collision);
    printf("      ===========================\n");
    printf("\n");
    printf("               Time Used\n");
    printf("=======================================\n");
    printf(" Running time:    %7.3lf s  =%5d ms\n", (double)(t2 - t0) / CLOCKS_PER_SEC, t2 - t0);
    printf("  >> Reading time:%7.3lf s  =%5d ms\n", (double)(t1 - t0) / CLOCKS_PER_SEC, t1 - t0);
    printf("  >> Sorting time:%7.3lf s  =%5d ms\n", (double)(t2 - t1) / CLOCKS_PER_SEC, t2 - t1);
    printf("=======================================\n");
    printf("------------------------------------------\n");

    fee_wordset(w_set);
    return 0;
}


void throw(Exception e) {
    switch (e) {  // catch the exception thrown
        case NO_EXCEPTION:
            printf(" >> Exception: No exception! (No need to throw this)\n");
            break;
        case MEMORY_ALLOCATION_EXCEPTION:
            printf(" >> Exception: Memory allocation failed!\n");
            break;
        case MEMORY_RELEASE_EXCEPTION:
            printf(" >> Exception: Memory release failed!\n");
            break;
        case FILE_OPENING_EXCEPTION:
            printf(" >> Exception: File opening failed!\n");
            break;
        case WORD_SET_FULL_EXCEPTION:
            printf(" >> Exception: Word set full!\n");
            break;
        default:
            printf(" >> Exception : Unknown exception!\n");
            break;
    }
    printf("------------------------------------------\n");
    exit(e);  // quit the program
}

void clear_buffer(void) {
    while (getc(stdin) != '\n');
}

void free_pointer(void *pointer) {
    if (pointer == NULL) {
        throw(MEMORY_RELEASE_EXCEPTION);
    } else {
        free(pointer);
    }
}

HashInt hash_word(char *word) {
    HashInt hash = 100007;
    int i = 0;
    while (word[i] != '\0') {
        hash = ((hash + word[i]) * word[i ++]) % WORD_TABLE_SIZE;
    }
    return hash;
}

HashInt probing_hash(HashInt hash, CountingInt pb) {
    return (31 * hash + 13 * pb + 107 * pb * pb) % (WORD_TABLE_SIZE - pb);  // quadratic probing
}

WordSet *new_wordset(void) {
    WordSet *set = (WordSet *)malloc(sizeof(WordSet));
    if (set == NULL) {
        throw(MEMORY_ALLOCATION_EXCEPTION);
    }
    set->w_table = (Word **)calloc(WORD_TABLE_SIZE, sizeof(Word *));
    if (set->w_table == NULL) {
        throw(MEMORY_ALLOCATION_EXCEPTION);
    }
    set->hashes = (HashInt *)malloc(MAX_DIFFERENT_WORDS * sizeof(HashInt));
    if (set->hashes == NULL) {
        throw(MEMORY_ALLOCATION_EXCEPTION);
    }
    set->length = 0;
    set->total = 0;
    return set;
}

void ask_filename(char *filename) {
    printf("Please type filename > ");
    scanf("%s", filename);
    clear_buffer();
}

void read_file(WordSet *set, char *filename) {
    // open file
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        throw(FILE_OPENING_EXCEPTION);
    }

    char line_buffer[LINE_BUFFER_SIZE];
    char ch;
    char word[MAX_WORD_LENGTH];
    int w_len = 0;
    HashInt hash;
    CountingInt probing;

    // read file
    while (fgets(line_buffer, sizeof(line_buffer), file)) {  // read lines
        for (int i = 0; line_buffer[i] != '\0'; ++ i) {  // traverse characters in line_buffer
            ch = line_buffer[i];
            if (isalpha(ch) != 0 || ch == '\'') {
                word[w_len ++] = ch;
            } else if (w_len >= MIN_WORD_LENGTH) {
                word[w_len] = '\0';
                w_len = 0;
                ++ set->total;
                strcpy(word, strupr(word));
                probing = 0;
                hash = hash_word(word);
                // printf("hash = %ld\n", hash);
                while (set->w_table[hash] != 0) {  // catch empty spots
                    if (strcmp(word, set->w_table[hash]->word) == 0) {  // catch words appeared
                        ++ set->w_table[hash]->times;
                        // printf("\"%s\" +1, times: %d\n", word, set->w_table[hash]->times);
                        break;
                    }
                    if (++ probing == set->length) {  // catch table full
                        printf("probing = set->length = %d\n", probing);
                        printf("Fill rate: %.3lf %%\n", 100 * (double)set->length / WORD_TABLE_SIZE);
                        throw(WORD_SET_FULL_EXCEPTION);
                    }
                    if (longest_probing < probing) {
                        longest_probing = probing;
                    }
                    ++ total_collision;
                    hash = probing_hash(hash, probing);  // calculate the next hash value with probing
                    // printf("probing_hash = %ld\n", hash);
                }
                if (set->w_table[hash] == 0) {  // catch words didn't appear before
                    // printf("word: %s, hash: %ld\n", word, hash);
                    set->w_table[hash] = (Word *)malloc(sizeof(Word));
                    if (set->w_table[hash] == NULL) {
                        throw(MEMORY_ALLOCATION_EXCEPTION);
                    }
                    set->w_table[hash]->times = 1;
                    strcpy(set->w_table[hash]->word, word);
                    set->hashes[set->length ++] = hash;
                }
            }
        }
    }

    // close file
    fclose(file);
}

void counting_sort_mf_words(WordSet *set, Word *mf_words, int mf_len) {
    CountingInt set_len = set->length;
    HashInt temp_hash;
    CountingInt temp_times;
    CountingInt temp_n;
    CountingInt i, j;

    CountingInt max_t = set->w_table[set->hashes[0]]->times;  // max_t = max_times
    for (i = 1; i < set_len; ++ i) {  // find the maximum value of times
        if (set->w_table[set->hashes[i]]->times > max_t) {
            max_t = set->w_table[set->hashes[i]]->times;
        }
    }
    // printf("max_t: %d\n", max_t);

    typedef struct {  // two-dimensional array of structures
        HashInt *h;  // h = hash values
        CountingInt n;  // n = length of h
    } CountingArray;
    CountingArray *c_arr = (CountingArray *)malloc((max_t + 1) * sizeof(CountingArray));
    if (c_arr == NULL) {
        throw(MEMORY_ALLOCATION_EXCEPTION);
    }

    for (i = 0; i < max_t + 1; ++ i) {  // fill c_arr[].n with zeros and allocate memory for c_arr[].h
        c_arr[i].h = (HashInt *)malloc(H_SIZE_INCREMENT * sizeof(HashInt));
        if (c_arr[i].h == NULL) {
            throw(MEMORY_ALLOCATION_EXCEPTION);
        }
        c_arr[i].n = 0;
    }

    for (i = 0; i < set_len; ++ i) {  // traverse and count the word table
        temp_hash = set->hashes[i];
        temp_times = set->w_table[temp_hash]->times;
        temp_n = c_arr[temp_times].n;
        // printf("times: %d, n: %d\n", temp_times, temp_n);
        if (temp_n % H_SIZE_INCREMENT == 0) {  // in case the memory of c_arr[].h is used up
            // printf("new size: %d\n", H_SIZE_INCREMENT * (temp_n / H_SIZE_INCREMENT) + 1);
            c_arr[temp_times].h = (HashInt *)realloc(c_arr[temp_times].h, ((temp_n / H_SIZE_INCREMENT) + 1) * H_SIZE_INCREMENT * sizeof(HashInt));
            if (c_arr[temp_times].h == NULL) {
                throw(MEMORY_ALLOCATION_EXCEPTION);
            }
        }
        c_arr[temp_times].h[c_arr[temp_times].n ++] = temp_hash;
    }

    int mf_index = 0;
    for (i = max_t; i >= 0; -- i) {  // the nested for loops to move the most frequent words to mf_words
        for (j = c_arr[i].n; j > 0; -- j) {
            temp_hash = c_arr[i].h[j - 1];
            // printf("word: %s, hash: %ld,\n\tn: %d, times: %d\n", set->w_table[temp_hash]->word, temp_hash, c_arr[i].n, i);
            // printf("word: %s, times: %d\n", set->w_table[temp_hash]->word, set->w_table[temp_hash]->times);
            mf_words[mf_index ++] = *set->w_table[temp_hash];
            if (mf_index == mf_len) {
                return;
            }
        }
    }

    for (i = 0; i < max_t + 1; ++ i) {
        free_pointer(c_arr[i].h);
    }
    free_pointer(c_arr);
}

void fee_wordset(WordSet *set) {
    for (CountingInt i = 0; i < set->length; ++ i) {
        free_pointer(set->w_table[set->hashes[i]]);
    }
    free_pointer(set->w_table);
    free_pointer(set->hashes);
    free_pointer(set);
}
