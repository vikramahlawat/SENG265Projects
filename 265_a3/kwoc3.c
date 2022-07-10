/*
 * kwoc3.c
 *
 * Starter file provided to students for Assignment #3, SENG 265,
 * Spring 2020
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "emalloc.h"
#include "listy.h"


void print_word(node_t *node, void *arg)
{
    char *format = (char *)arg;
    printf(format, node->text);
}

char* capitalize(char* str) {
	int len = strlen(str);
	char* chr = emalloc(sizeof(char)*(len + 1));
	int i = 0;
	for(i = 0; i < len; i++)  {
		chr[i] = toupper(str[i]);
	}
	chr[i] = '\0';
	return chr;
}

int main(int argc, char *argv[])
{
    char *keyword_file = NULL;
    char *input_file = NULL;
	node_t* keyword_head = NULL;
	node_t* sentence_head = NULL;
    int i = 1;

    while(i < argc) {
        if (strcmp(argv[i], "-e") == 0 && i + 1 <= argc) {
            keyword_file = argv[i+1];
			FILE* fp = fopen(keyword_file, "r");
			if (fp == NULL) {
				printf("Error while opening file %s", keyword_file);
				exit(1);
			}
			else {
				char buffer[2048];
				while (fgets(buffer, 2048, fp) != NULL) {
					node_t* temp_node = new_node(strtok(buffer, "\n"));
					keyword_head = add_end(keyword_head, temp_node);
				}
				fclose(fp);
			}
			i += 2;
        } else {
            input_file = argv[i];
			FILE* fp = fopen(input_file, "r");
			if (fp == NULL) {
				printf("Error while opening file %s", input_file);
				exit(1);
			}
			else {
				char buffer[2048];
				while (fgets(buffer, 2048, fp)) {
					node_t* temp_node = new_node(strtok(buffer, "\n"));
					sentence_head = add_end(sentence_head, temp_node);
				}
				fclose(fp);
			}
			i++;
        }
    }

	// Iterating over each keyword
	node_t* kcurr = keyword_head, *scurr = sentence_head;
	while (kcurr != NULL) {
		int sentenceNo = 0;
		scurr = sentence_head;
		char* capitalizedKeyword = capitalize(kcurr->text);
		while (scurr != NULL) {
			char* keyword = kcurr->text;
			char* sentence = scurr->text;
			int cnt = 0;
			char* pos = sentence;
			while (1) {
				pos = strstr(pos , keyword);
				if (pos == NULL) {
					break;
				}
				else {
					int isSpaceBefore = pos == sentence ? 1 : (*(pos - 1) == ' ');
					int isSpaceAfter = sentence - pos - strlen(keyword) > 0 ? *(pos + strlen(keyword)) == ' ' : 1;
					if (isSpaceBefore && isSpaceAfter) {
						cnt++;
					}
					pos += strlen(keyword);
				}
			}
			if (cnt > 0) {
				sentenceNo++;
				if (cnt > 1) {
					printf("%s\t%s (%d*)\n", capitalizedKeyword, sentence, sentenceNo);
				}
				else {
					printf("%s\t%s (%d)\n", capitalizedKeyword, sentence, sentenceNo);
				}
			}
			scurr = scurr->next;
		}
		kcurr = kcurr->next;
		free(capitalizedKeyword);
	}

	kcurr = keyword_head;
	while (kcurr != NULL) {
		kcurr = remove_front(kcurr);
	}
	scurr = sentence_head;
	while (scurr != NULL) {
		scurr = remove_front(scurr);
	}
}
                                                                           
