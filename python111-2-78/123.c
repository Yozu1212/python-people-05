#include <stdio.h> 
#define STUDENTS 3 
#define EXAMS 4

int minimum(const int grades [][EXAMS], size_t pupils, size_t tests);
int maximum(const int gradest[][EXAMS], size_t pupils,size_t tests);
double average(const int setofGrades[], size_t tests);
void printArray (const int grades[][EXAMS], size_t pupils, size_t tests);

int main(void)
{
int studentGrades[STUDENTS][EXAMS]={	{ 77, 68, 86, 73},
										{ 96, 87, 89, 78 },
										{ 70, 90, 86, 81 }};

puts ("The array is:");
printArray(studentGrades, STUDENTS, EXAMS);

printf("\n\nLowest grade: %d\nHighest grade: %d\n", 
minimum(studentGrades, STUDENTS, EXAMS),
maximum(studentGrades, STUDENTS, EXAMS));

for (size_t student = 0; student < STUDENTS; ++student) {
printf ("The average grade for student %u is %.2f\n",
 student, average(studentGrades [student], EXAMS));
}
}

int minimum(const int grades [][EXAMS], size_t pupils, size_t tests){
int lowGrade = 100; 
for (size_t i = 0; i < pupils; ++i) { 
for (size_t j = 0; j <tests; ++j) {
if (grades [i][j] < lowGrade) {
lowGrade = grades[i][j];
}
}
}
return lowGrade; 
}





int maximum(const int grades [][EXAMS], size_t pupils, size_t tests)
{
int highGrade = 0; 
for (size_t i = 0; i < pupils; ++i) {
for (size_t j = 0; j < tests; ++j) {
if (grades[i][j] > highGrade) {
highGrade = grades[i][j];
}
}
}
return highGrade; 
}




double average (const int setofGrades[], size_t tests)
{
int total = 0;
for (size_t i = 0; i < tests; ++i) { 
total += setofGrades[i];
}

return (double) total / tests; 
}




void printArray(const int grades[][EXAMS], size_t pupils, size_t tests)
{
printf("%s","                     [0]  [1]  [2]  [3]");
for (size_t i = 0; i < pupils; ++i){
printf("\nstudentGrades [%u] ", i);
for (size_t j = 0; j <tests; ++j) { 
printf ("%5d",grades[i][j]);
}
}
}
