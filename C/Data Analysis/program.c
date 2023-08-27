/**
 * This project downloads stock data from Yahoo Finance.
 * 
 * @author Ben Antonellis
*/

#include <stdio.h>
#include <stdlib.h>

#include "downloader.h"
#include "analyze.h"

int main(int argc, char** argv) {

    // Code for one singular query

    char* result = (char*)malloc(256);
    if (FormatQueryString(result, "SPY", "2020-09-01", "2020-10-01", "1mo") > 0) {
        printf("Error in FormatQueryString\n");
        exit(1);
    }
    DownloadData(result, 0);
    free(result);
    PrintData(result);
    

    // Code for multiple queries

    /*
    int queries = 5;
    char tickers[queries][3];
    char from[11];
    char to[11];
    char interval[3];
    printf("Enter tickers. \n");
    for (int i = 0; i < queries; i++) {
        char input[4];
        printf(">>> ");
        scanf("%s", input);
        strcpy(tickers[i], input);
    }
    printf("Enter from date: ");
    scanf("%s", from);
    printf("Enter to date: ");
    scanf("%s", to);
    printf("Enter interval: ");
    scanf("%s", interval);

    for (int i = 0; i < queries; i++) {
        char* result = (char*)malloc(256);
        if (FormatQueryString(result, tickers[i], from, to, interval) > 0) {
            printf("Error in FormatQueryString\n");
            exit(1);
        }
        DownloadData(result, 1);
        free(result);
    }

    */

    return 0;

}