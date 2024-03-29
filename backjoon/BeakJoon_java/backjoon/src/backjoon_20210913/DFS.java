package backjoon_20210913;

import java.util.ArrayList;

public class DFS {

	public static int[][] graph;
	public static int[] degree;
	public static int[] visited;
	public static ArrayList<Integer> sortGraph;

	
	
	public void dfs(int num) {
		visited[num] = 1;
		for(int i = 0; i < graph[num].length; i++) {
			if(graph[num][i] == 1 && visited[i] == 0) {
				dfs(i);
			}
		}
		sortGraph.add(num);
	}
	

	public void sortDFS() {
		for (int i = 0; i < graph.length; i++) {
			if(visited[i] == 0) {
				dfs(i);
			}
		}
	}
}
