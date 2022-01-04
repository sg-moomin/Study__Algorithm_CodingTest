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
 * [���� �ȵǴ� ����]
 * Q. ���ʿ� ���� ������ �����ϴ� ���θ� ��� ��η� ����ȴ�.
 * Q. � ���п����� ��� ���б��� �̵� ���� 
 * Q. �ִܰŸ��� ���̸� ���ϸ�ȴ� -> �ּ� ���� Ʈ�� -> �ּ� ���д� Ʈ��
 * Q. ����б��� �����ϴ� ��ΰ� ���� ��� -1�� ����Ѵ�.
 * 
 * 
 * 
 * */

class school implements Comparable<school>{

	int fristNode;
	int endNode;
	int result;
	
	school(int fristNode, int endNode, int result){
		this.fristNode = fristNode;
		this.endNode = endNode;
		this.result = result;
	}
	
	@Override
	public int compareTo(school o) {
		return result - o.result;
	}
}


public class backjoon_14621 {

	
	static int[] parent;
	static ArrayList<school> Nodes;
	
	// union-find �����
	public static int find(int answer) {
		if(parent[answer] == answer) {
			return answer;
		} else {
			return parent[answer] = find(parent[answer]);
		}
	}
	
	public static void union(int x, int y) {
		x = find(x);
		y = find(y);
		if(y != x) parent[y] = x;
	}
	
	// kruskal
	public static int kruskal(int m) {
		parent = new int[m + 1];
		
		for(int i = 1; i <= m; i++) {
			parent[i] = i;
		}


		Collections.sort(Nodes);
		int result = 0;
		int schoolCount = 0;
		
		for(school node : Nodes) {
			school schoolNode = node;
			
			if(find(schoolNode.fristNode) != find(schoolNode.endNode)) {
				union(schoolNode.fristNode, schoolNode.endNode);
				result += schoolNode.result;
				schoolCount++;
			}
		}
		
		if(schoolCount == m - 1) return result;
		else return -1;
	}
	
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer stringTk;
	
		stringTk = new StringTokenizer(reader.readLine());
		int N = Integer.parseInt(stringTk.nextToken());
		int M = Integer.parseInt(stringTk.nextToken());
		
		String[] sex = new String[N+1];
		Nodes = new ArrayList<school>();
		String checkSex = reader.readLine();
		stringTk = new StringTokenizer(checkSex);
		
		for(int i = 1; i <= N; i++) {
			sex[i] = stringTk.nextToken();
		}
		
		for(int i = 0; i < M; i++) {
			stringTk = new StringTokenizer(reader.readLine());
			int u = Integer.parseInt(stringTk.nextToken());
			int v = Integer.parseInt(stringTk.nextToken());
			int d = Integer.parseInt(stringTk.nextToken());
			
			if(!sex[u].equals(sex[v])) {
				Nodes.add(new school(u, v, d));
			}
		}
		
		int result = kruskal(N);
		
		writer.write(result + "\n");
		writer.flush();
		writer.close();
		reader.close();
		
	}
}
