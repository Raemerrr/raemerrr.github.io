#include <iostream>
#include <queue>
#include <string>
#include <algorithm>
#include <set>

using namespace std;
string N;
int K, M, MAX;

void Proc()
{
	int currCnt = 0;
	queue<string> q;
	q.emplace(N);
	int MAX = 0;
	while (!q.empty() && currCnt < K)
	{
		set<string> visited;
		//한 사이클 시작
		for (int z = 0, size = q.size(); z < size; z++)
		{
			string front = q.front();
			q.pop();
			for (int i = 0; i < M - 1; i++)
			{
				for (int j = i + 1; j < M; j++)
				{
					if (front[j] == '0' && i == 0) { continue; }
					swap(front[i], front[j]);
					if (visited.find(front) == visited.end())
					{
						if (currCnt + 1 == K && MAX < stoi(front))
						{
							MAX = stoi(front);
						}
						visited.emplace(front);
						q.emplace(front);
					}
					swap(front[i], front[j]);
				}
			}
		}
		//한 사이클 종료
		currCnt++;
	}
	if (currCnt != K) { cout << "-1\n";	return; }
	cout << MAX << "\n";
	return;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> K;
	M = N.size();
	if (M == 1 || (stoi(N) % 10 == 0 && M == 2))
	{
		cout << "-1\n";
		return 0;
	}
	Proc();
	return 0;
}
