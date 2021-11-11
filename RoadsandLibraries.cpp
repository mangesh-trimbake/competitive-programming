#include <bits/stdc++.h> 

using namespace std;

int mx = INT_MAX;

const int arr_limit = 1e7+10;

//int arr[arr_limit];

const int graph_v_limit = 1e5+10;


vector<int> g[graph_v_limit];

vector<int> current_cc;

bool visited[graph_v_limit];

void dfs(int vertex){

	// cout << vertex<< endl;
	visited[vertex] = 1;
	current_cc.push_back(vertex);
	for(auto child : g[vertex]){

		if(visited[child]) continue;

		dfs(child);
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

void clear_graph(int n){
	for(int i=1;i<=n;++i){
		g[i].clear();
		visited[i]=0;
	}
}



int main(){

	// int l = sizeof(g)/sizeof(g[0]);

	// cout<< "hello world " << l << typeid(g[0]).name() << endl;

	// cout<< mx;

	int t;
	cin >> t;
	while(t--){

		// vector<int> g[graph_v_limit];
		// g.clear()
		// for (auto& v : g) {
		//    v.clear();
		// }

		// bool visited[graph_v_limit];	
		// visited.clear()
		int n,m,c_lib,c_road;
		cin >> n >> m>>c_lib>>c_road;
		// cout << n<<" "<<m<< " "<<c_lib<<" "<<c_road<<endl



		for(int i=0; i<m;++i){
			int v1,v2;
			cin >> v1 >>v2;
			g[v1].push_back(v2);
			g[v2].push_back(v1);
		}

		if(c_lib<c_road || m==0) {
			// cout << " inside";
			cout << c_lib*1LL*n<<endl;
			clear_graph(n);
			continue;
		}


		// cout << has_cycle(0) << endl;

		int connected_cities = 0;
		long long int cost = 0;
		for(int i=1;i<=n;++i){

			if(visited[i]) continue;
			current_cc.clear();
			dfs(i);
			connected_cities++;
			
			cost+=(c_lib + ((current_cc.size()-1)*1LL*c_road));
		}
		cout << cost<<endl;

		clear_graph(n);



		
		
	}


	return 0; 
}