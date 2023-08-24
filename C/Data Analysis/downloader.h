/**
 * Data Downloader Implementation.
 * 
 * @author Ben Antonellis
*/

#include <curl/curl.h>
#include <curl/easy.h>
#include <string.h>
#include <stdio.h>
#include <time.h>

#define DOWNLOAD_PATH "/tmp/stock_data.txt"

int DateToUnix(char* date) {
    struct tm tm;
    time_t epoch;
    if (strptime(date, "%Y-%m-%d", &tm) != NULL) {
        epoch = mktime(&tm);
    }
    return epoch;
}

int FormatQueryString(char* result, char* ticker, char* start_time, char* end_time, char* interval) {
    char* res;
    time_t from = DateToUnix(start_time);
    time_t to = DateToUnix(end_time);
    if (0 > asprintf(
        &res,
        "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%ld&period2=%ld&interval=%s&events=history", 
        ticker,
        from,
        to,
        interval)) return 1;
    strcpy(result, res);
    return 0;
}

size_t WriteData(void* ptr, size_t size, size_t n, FILE* stream) {
    size_t written = fwrite(ptr, size, n, stream);
    return written;
}

void DownloadData(char* url) {
    CURL* curl;
    FILE* file;
    CURLcode result;

    curl = curl_easy_init();
    if (!curl) {
        printf("Error in DownloadData.\n");
        exit(1);
    }

    file = fopen(DOWNLOAD_PATH, "wb");
    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteData);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, file);
    result = curl_easy_perform(curl);
    //fprintf(file, "\n");
    curl_easy_cleanup(curl);
    fclose(file);

}