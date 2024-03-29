package backjoon_20210913;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class BFS {

	public static int[][] graph;
	public static int[] indegree;
	public static ArrayList<Integer> sortGraph;
	
	
	public void bfs() {
		Queue<Integer> Que = new LinkedList<Integer>();
		
		for(int i = 0; i < indegree.length; i++) {
			if(indegree[i] == 0) {
				indegree[i]--;
				sortGraph.add(i);
				Que.add(i);
			}
		}
		
		while(!Que.isEmpty()) {
			int node = Que.poll();
			
			for(int j = 0; j < graph.length; j++) {
				if(graph[node][j] == 1) {
					graph[node][j] = 0;
					indegree[j]--;
				}
				
				if(indegree[j] == 0) {
					indegree[j]--;
					sortGraph.add(j);
					Que.add(j);
				}
			}
		}
	}
	
	public void sortBFS() {
		for (int i = 0; i < graph.length; i++) {
			for(int j = 0; j < graph.length; j++) {
				if(graph[i][j] == 1) {
					indegree[j]++;
				}
			}
		}
		
		bfs();
	}
	
}
