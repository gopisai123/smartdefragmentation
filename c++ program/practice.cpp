// #include <stdio.h>
// #include <stdlib.h>

// #define MAX_N 100 // Maximum number of ingredient boxes

// // Helper function to compare integers for qsort
// int compare(const void *a, const void *b) {
//     return (*(int*)a - *(int*)b);
// }

// // Function to check if we can prepare m meals with k adjacent boxes by day `day_limit`
// int canPrepareMeals(int availabilityDay[], int n, int m, int k, int day_limit) {
//     int count = 0;

//     // Array to keep track of available ingredient boxes up to `day_limit`
//     int available_boxes[MAX_N];
//     int available_count = 0;

//     // Collect all available boxes up to `day_limit`
//     for (int i = 0; i < n; i++) {
//         if (availabilityDay[i] <= day_limit) {
//             available_boxes[available_count++] = availabilityDay[i];
//         }
//     }

//     // Check if we have enough k adjacent boxes
//     if (available_count < m * k) {
//         return 0; // Not enough boxes
//     }

//     // Sort the available boxes
//     qsort(available_boxes, available_count, sizeof(int), compare);

//     // Check for m meals
//     for (int i = 0; i <= available_count - k; i++) {
//         // Check if there's a valid window of k adjacent boxes
//         int possible_meals = 0;
//         for (int j = i; j < i + k; j++) {
//             if (j < available_count && (j == i || available_boxes[j] == available_boxes[j-1] + 1)) {
//                 possible_meals++;
//             }
//         }
//         if (possible_meals >= k) {
//             int meals_possible = 0;
//             for (int j = i; j <= available_count - k; j++) {
//                 if (available_boxes[j + k - 1] <= day_limit) {
//                     meals_possible++;
//                 }
//                 if (meals_possible >= m) {
//                     return 1; // We can prepare m meals
//                 }
//             }
//         }
//     }

//     return 0; // Not possible to prepare the required number of meals
// }






int findMinimumDays(int availabilityDay[], int n, int m, int k) {
    int left = 1;
    int right = 100000; 
    int result = -1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (canPrepareMeals(availabilityDay, n, m, k, mid)) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1; 
        }
    }

    return result;
}

int main() {
    int n, m, k;
    scanf("%d", &n);

    int availabilityDay[MAX_N];
    for (int i = 0; i < n; i++) {
        scanf("%d", &availabilityDay[i]);
    }

    scanf("%d", &m);
    scanf("%d", &k);

    int result = findMinimumDays(availabilityDay, n, m, k);

    printf("%d\n", result);

    return 0;
}








// #include <stdio.h>
// #include <string.h>
// int binarySearch(char countries[][50], int n, char* target) {
//     int left = 0, right = n - 1;

//     while (left <= right) {
//         int mid = left + (right - left) / 2;
        
//         int comparison = strcmp(countries[mid], target);
//         if (comparison == 0) {
//             return mid; 
//         } else if (comparison < 0) {
//             left = mid + 1; 
//         } else {
//             right = mid - 1; 
//         }
//     }
    
//     return -1; 
// }

// int main() {
//     int n;
//     scanf("%d", &n);

//     char countries[n][50];
//     for (int i = 0; i < n; i++) {
//         scanf("%s", countries[i]);
//     }

//     char target[50];
//     scanf("%s", target);

//     int result = binarySearch(countries, n, target);

//     if (result != -1) {
//         printf("The country %s is found at index %d.\n", target, result);
//     } else {
//         printf("%s is not found.\n", target);
//     }

//     return 0;
// }








// #include <stdio.h>
// int canShipWithinDays(int* weights, int n, int days, int capacity) {
//     int dayCount = 1;
//     int currentLoad = 0;

//     for (int i = 0; i < n; i++) {
//         if (currentLoad + weights[i] > capacity) {
//             dayCount++;
//             currentLoad = weights[i];
//             if (dayCount > days) {
//                 return 0;
//             }
//         } else {
//             currentLoad += weights[i];
//         }
//     }
//     return 1;
// }

// int findMinCapacity(int* weights, int n, int days) {
//     int low = 0, high = 0;
//     for (int i = 0; i < n; i++) {
//         if (weights[i] > low) low = weights[i]; 
//         high += weights[i]; 
//     }

//     while (low < high) {
//         int mid = low + (high - low) / 2;
//         if (canShipWithinDays(weights, n, days, mid)) {
//             high = mid;
//         } else {
//             low = mid + 1;
//         }
//     }

//     return low;
// }

// int main() {
//     int n;
//     scanf("%d", &n);

//     int weights[n];
//     for (int i = 0; i < n; i++) {
//         scanf("%d", &weights[i]);
//     }

//     int days;
//     scanf("%d", &days);

//     int result = findMinCapacity(weights, n, days);
//     printf("%d\n", result);

//     return 0;
// }




