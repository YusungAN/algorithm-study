#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100000

void swap(int* a, int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

typedef struct {
	int heap[MAX_SIZE];
	int count;
} PriorityQueue;

void push(PriorityQueue* pq, int data)
{
	if (pq->count >= MAX_SIZE) return;
	pq->heap[pq->count] = data;
	int now = pq->count;
	int parent = (pq->count - 1) / 2;
	while (now > 0 && pq->heap[now] > pq->heap[parent]) {
		swap(&pq->heap[now], &pq->heap[parent]);
		now = parent;
		parent = (parent - 1) / 2;
	}

	pq->count++;
}

int pop(PriorityQueue* pq) {
	if (pq->count <= 0) return -99999;
	int res = pq->heap[0];
	pq->count--;
	pq->heap[0] = pq->heap[pq->count];

	int now = 0, left_child = 1, right_child = 2;
	int target = now;
	while (left_child < pq->count) {
		if (pq->heap[target] < pq->heap[left_child]) target = left_child;
		if (pq->heap[target] < pq->heap[right_child] && right_child < pq->count) target = right_child;
		if (target == now) break;
		else {
			swap(&pq->heap[now], &pq->heap[target]);
			now = target;
			left_child = now * 2 + 1;
			right_child = now * 2 + 2;
		}
	}
	return res;
}

int main(void) {
	PriorityQueue lq;
	PriorityQueue rq;
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