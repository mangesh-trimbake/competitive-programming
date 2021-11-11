#include <bits/stdc++.h> 

using namespace std;

int mx = INT_MAX;

const int arr_limit = 1e7+10;

//int arr[arr_limit];

const int graph_v_limit = 1e5+10;


vector<int> g[graph_v_limit];

bool visited[graph_v_limit];

int level[graph_v_limit];


queue<int> child_queue;

void dfs(int vertex){

	cout << vertex<< endl;
	visited[vertex] = 1;
	for(auto child : g[vertex]){

		if(visited[child]) continue;

		dfs(child);
	}

}

void bfs_r(int vertex){


	// root node condtion
	if(child_queue.empty() && !visited[vertex]){
		visited[vertex] = 1;
		cout << vertex << endl;
	}


	for(auto child : g[vertex]){
		if(visited[child]) continue;
		visited[child] =1;
		cout<<child<<endl;
		child_queue.push(child);
	}
	while(!child_queue.empty()){
		int f = child_queue.front();
		child_queue.pop();
		bfs_r(f);
	}

}

void bfs(int vertex){


	// root node condtion
	if(child_queue.empty() && !visited[vertex]){
		visited[vertex] = 1;
		level[vertex]=0;
		child_queue.push(vertex);
	}


	
	while(!child_queue.empty()){
		int f = child_queue.front();
		child_queue.pop();
		
		cout<< f<<" level:"<<level[f]<< endl;

		for(auto child : g[f]){
			if(visited[child]) continue;
			visited[child] =1;
			level[child] = level[f]+1;
			child_queue.push(child);
		}
	}

}




bool has_cycle(int vertex){

	cout << vertex<< endl;
	visited[vertex] = 1;
	for(auto child : g[vertex]){

		if(visited[child]){
			cout<<" making cycle";
			return true;
		}

		has_cycle(child);
	}

	cout << " oustside for";
	return false;

}



int main(){

	// int l = sizeof(g)/sizeof(g[0]);

	// cout<< "hello world " << l << typeid(g[0]).name() << endl;

	// cout<< mx;

	int v,e;
	cin >> v >> e;

	for(int i=0; i<e;++i){
		int v1,v2;
		cin >> v1 >>v2;
		g[v1].push_back(v2);
		g[v2].push_back(v1);
	}
	// visited[1] = 1;
	// bfs_r(1);
	bfs(1);

	// cout << has_cycle(0) << endl;


	

	return 1; 
}