#include <iostream>
#include <vector>

using namespace std;

int N, ans;
vector<vector<int>> dp;
vector<vector<int>> map;

void Func()
{
	dp[1][1] = map[1][1];
	for (int i = 2; i <= N; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			//���� ���� ���
			if (j == 1)
			{
				dp[i][j] = dp[i - 1][j] + map[i][j];
			}
			//���� ���� ���
			else if (j == i)
			{
				dp[i][j] = dp[i - 1][j - 1] + map[i][j];
			}
			//�߰��� �ִ� ���
			else
			{
				//dp[i - 1][j] + map[i][j] : �� ��ܿ��� ������ ���
				//dp[i - 1][j - 1] + map[i][j] : �� ��ܿ��� ������ ���
				dp[i][j] = (dp[i - 1][j] + map[i][j] > dp[i - 1][j - 1] + map[i][j]) ? dp[i - 1][j] + map[i][j] : dp[i - 1][j - 1] + map[i][j];
			}
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	map = vector<vector<int>>(N + 1, vector<int>(N + 1, 0));
	dp = vector<vector<int>>(N + 1, vector<int>(N + 1, 0));
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			cin >> map[i][j];
		}
	}
	Func();
	for (int i = 1; i <= N; i++)
	{
		ans = (ans > dp[N][i]) ? ans : dp[N][i];
	}
	cout << ans << "\n";
	return 0;
}