#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct _GNode {
	int id;
	char alphabet;
	struct _GNode* next;
} GNode;

typedef struct {
	int num;
	GNode** heads;
} Graph;

void CreateGraph(Graph* pgraph, int num) {
	pgraph->num = num;
	pgraph->heads = (GNode**)malloc(sizeof(GNode*) * num);
	for (int i = 0; i < num; i++) {
		pgraph->heads[i] = (GNode*)malloc(sizeof(GNode));
		pgraph->heads[i]->next = NULL;
	}

}

void DestroyGraph(Graph* pgraph) {
	for (int i = 0; i < pgraph->num; i++) {
		GNode* cur = pgraph->heads[i];
		while (cur != NULL) {
			GNode* temp = cur;
			cur = cur->next;
			free(temp);
		}
	}
	free(pgraph->heads);
}

void AddEdge(Graph* pgraph, int src, int dest, char src_char, char dest_char) {
	GNode* newNode1, * newNode2, * cur;
	newNode1 = (GNode*)malloc(sizeof(GNode));
	newNode1->id = dest;
	newNode1->alphabet = dest_char;
	newNode1->next = NULL;
	cur = pgraph->heads[src];
	while (cur->next != NULL)
		cur = cur->next;
	cur->next = newNode1;
	newNode2 = (GNode*)malloc(sizeof(GNode));
	newNode2->id = src;
	newNode2->alphabet = src_char;
	newNode2->next = NULL;
	cur = pgraph->heads[dest];
	while (cur->next != NULL)
		cur = cur->next;
	cur->next = newNode2;
}

Graph graph;
int char_visited[26];
int visited[400];
int ccnt = 0;

void DFS(GNode *n, int cnt) {
	if (char_visited[n->alphabet - 65] || visited[n->id]) {
		if (ccnt < cnt) ccnt = cnt;
		return;
	}

	char_visited[n->alphabet - 65] = 1;
	visited[n->id] = 1;
	GNode* cur = graph.heads[n->id]->next;
	while (cur != NULL) {
		DFS(cur, cnt + 1);
		cur = cur->next;
	}

	char_visited[n->alphabet - 65] = 0;
	visited[n->id] = 0;
}

int main() {
	int r, c;
	scanf("%d %d", &r, &c);
	CreateGraph(&graph, r*c);
	char temp[20][21];
	for (int y = 0; y < r; y++) {
		scanf("%s", temp[y]);
		for (int x = 0; x < c; x++) {
			if (y > 0) {
				AddEdge(&graph, c * y + x, c * (y - 1) + x, temp[y][x], temp[y - 1][x]);
			}
			if (x < c - 1) {
				AddEdge(&graph, c * y + x, c * y + x + 1, temp[y][x], temp[y][x + 1]);
			}
		}
	}
	GNode root = { 0, temp[0][0], -1 };

	DFS(&root, 1);
	printf("%d\n", ccnt - 1);
	DestroyGraph(&graph);
}
