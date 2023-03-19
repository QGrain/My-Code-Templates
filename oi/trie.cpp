#include <iostream>
using namespace std;

const int MAXN = 100005;
int trie[MAXN][26], idx = 0;
bool is_end[MAXN];

void insert(string s) {   // 插入字符串
    int p = 0;
    for(auto c : s) {
        int u = c - 'a';
        if(!trie[p][u]) trie[p][u] = ++idx;
        p = trie[p][u];
    }
    is_end[p] = true;
}

bool find(string s) {   // 查找字符串
    int p = 0;
    for(auto c : s) {
        int u = c - 'a';
        if(!trie[p][u]) return false;
        p = trie[p][u];
    }
    return is_end[p];
}

void remove(string s) {   // 删除字符串
    int p = 0;
    for(auto c : s) {
        int u = c - 'a';
        if(!trie[p][u]) return;
        p = trie[p][u];
    }
    is_end[p] = false;
}

int main() {
    int n;
    cin >> n;

    for(int i = 1; i <= n; ++i) {
        string s;
        cin >> s;
        insert(s);
    }

    int m;
    cin >> m;

    for(int i = 1; i <= m; ++i) {
        string s;
        cin >> s;
        if(find(s)) cout << s << " exists in the trie." << endl;
        else cout << s << " does not exist in the trie." << endl;
    }

    remove("abc");
    cout << "After removing 'abc':" << endl;
    if(find("abc")) cout << "abc exists in the trie." << endl;
    else cout << "abc does not exist in the trie." << endl;

    return 0;
}