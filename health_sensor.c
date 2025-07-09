#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    FILE *fptr = fopen("sensor_data.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    srand(time(0));
    for (int i = 0; i < 10; i++) {
        int heartRate = rand() % 40 + 60;
        float temperature = (rand() % 30 + 360) / 10.0;
        fprintf(fptr, "%d,%.1f\n", heartRate, temperature);
    }

    fclose(fptr);
    printf("Sensor data generated.\n");
    return 0;
}
