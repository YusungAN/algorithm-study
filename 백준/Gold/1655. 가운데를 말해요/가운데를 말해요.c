#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100000

void nodeChange(int* a, int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

typedef struct priorityQueue
{
	int heap[MAX_SIZE];
	int count;
} priorityQueue;

void push(priorityQueue* root, int data)
{
	if (root->count >= MAX_SIZE) return;
	root->heap[root->count] = data;
	int now = root->count;
	int parent = (root->count - 1) / 2;
	while (now > 0 && root->heap[now] > root->heap[parent])
	{
		nodeChange(&root->heap[now], &root->heap[parent]);
		now = parent;
		parent = (parent - 1) / 2;
	}

	root->count++;
}

int pop(priorityQueue* root) {
	if (root->count <= 0) return -9999;
	int res = root->heap[0];
	root->count--;
	root->heap[0] = root->heap[root->count];

	int now = 0, leftChild = 1, rightChild = 2;
	int target = now;
	while (leftChild < root->count) {
		if (root->heap[target] < root->heap[leftChild]) target = leftChild;
		if (root->heap[target] < root->heap[rightChild] && rightChild < root->count) target = rightChild;
		if (target == now) break;
		else {
			nodeChange(&root->heap[now], &root->heap[target]);
			now = target;
			leftChild = now * 2 + 1;
			rightChild = now * 2 + 2;
		}
	}
	return res;
}

int main(void) {
	priorityQueue lq;
	priorityQueue rq;
	lq.count = 0;
	rq.count = 0;

	int n;
	scanf("%d", &n);
	int value;
	for (int i = 0; i < n; i++) {
		scanf("%d", &value);
		if (lq.count == rq.count) {
			push(&lq, value);
		}
		else {
			push(&rq, -1 * value);
		}

		int p, q;
		if (rq.count > 0 && lq.heap[0] > -1 * rq.heap[0]) {
			p = -1 * pop(&lq);
			q = -1 * pop(&rq);
			push(&lq, q);
			push(&rq, p);
		}
		printf("%d\n", lq.heap[0]);

	}
	return 0;
}