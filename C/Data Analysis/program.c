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

    char* result = (char*)malloc(256);
    if (FormatQueryString(result, "SPY", "2020-09-01", "2020-10-01", "1mo") > 0) {
        printf("Error in FormatQueryString\n");
        exit(1);
    }
    DownloadData(result);
    DateToUnix("2020-09-01");

    return 0;

}