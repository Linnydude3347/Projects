/**
 * Data Analyze Implementation.
 * 
 * @author Ben Antonellis
*/

#define DATE 0
#define OPEN 1
#define HIGH 2
#define LOW 3
#define CLOSE 4
#define ADJ_CLOSE 5
#define VOLUME 6

#define COLUMNS 7
const int COLUMN_NAMES[COLUMNS] = { DATE, OPEN, HIGH, LOW, CLOSE, ADJ_CLOSE, VOLUME };

char* GetData(char* line, int col) {
    char* token;
    for (token = strtok(line, ","); token && *token; token = strtok(NULL, "\n")) {
        if (!--col) {
            return token;
        }
    }
    return NULL;
}

void PrintData(char* line) {
    printf("%s\n", line);
}