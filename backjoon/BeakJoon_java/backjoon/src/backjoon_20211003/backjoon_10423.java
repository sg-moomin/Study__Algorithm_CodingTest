package backjoon_20211003;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

/**
 * [전기가 부족해]
 * Q. 3개의 발전소를 기준으로 도시를 연결한다. 
 * Q. 3개의 발전소를 먼저 체크한 뒤 동일하게 kruskal을 이용하여 연결한다.
 * Q. 마지막 남은 노드를 연결하는 선을 제외하는 방식이다.
 * 
 * 
 * */


class city implements Comparable<city>{

	int fristNode;
	int endNode;
	int result;
	
	city(int fristNode, int endNode, int result){
		this.fristNode = fristNode;
		this.endNode = endNode;
		this.result = result;
	}
	
	@Override
	public int compareTo(city o) {
		return result - o.result;
	}
}

public class backjoon_10423 {

	static int[] parent;
	static int[] ynyCity;
	static ArrayList<city> Nodes;
	
	public static int find(int answer) {
		if(parent[answer] ==  -1) {
			return -1;
		}
		if(parent[answer] == answer) {
			return answer;
		} else {
			return parent[answer] = find(parent[answer]);
		}
	}
	
	
	public static void union(int x, int y) {
		x = find(x);
		y = find(y);
		
		if(x == -1){
			parent[y] = x;
		} else if(y == -1) {
			parent[x] = y;
		}
		else if(y != x) {
			parent[y] = x;
		}
	}
	
	public static int kruskal(int m) {
		parent = new int[m + 1];
		
		for(int i = 1; i <= m; i++) {
			if(ynyCity[i] == -1) {
				parent[i] = -1;
			} else {
				parent[i] = i;
			}
		}
		
		Collections.sort(Nodes);
		
		for(int i = 0; i < Nodes.size(); i++) {
			System.out.println("node arr : " + Nodes.get(i).fristNode + " | " + Nodes.get(i).endNode + " | " + Nodes.get(i).result);
		}
		
		int answer = 0;
		
		for(city node : Nodes) {
			city cityNode = node;
			
			if(find(cityNode.fristNode) != find(cityNode.endNode)) {
				union(cityNode.fristNode, cityNode.endNode);
				answer += cityNode.result;
	
			}
		}
		
		return answer;
	}
	
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer stringTk;
	
		stringTk = new StringTokenizer(reader.readLine());
		int N = Integer.parseInt(stringTk.nextToken()); 
		int M = Integer.parseInt(stringTk.nextToken());
		int K = Integer.parseInt(stringTk.nextToken());
		
		ynyCity = new int[N+1];
		String cityCheck = reader.readLine();
		stringTk = new StringTokenizer(cityCheck);
		
		Nodes = new ArrayList<city>();
		
		for(int i = 1; i <= K; i++) {
			int num = Integer.parseInt(stringTk.nextToken());
			ynyCity[num] = -1;
		}
		
		
		for(int i = 0; i < M; i++) {
			stringTk = new StringTokenizer(reader.readLine());
			int u = Integer.parseInt(stringTk.nextToken());
			int v = Integer.parseInt(stringTk.nextToken());
			int w = Integer.parseInt(stringTk.nextToken());
			
			Nodes.add(new city(u, v, w));
		}
		
		
		int result = kruskal(N);
		
		
		writer.write(result + "\n");
		writer.flush();
		writer.close();
		reader.close();
		
		
		
		
		
	}

}
