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
 * [���³�]
 * Q. ���ε� �Ϻθ� �ҵ������� �շ��� �� ���� �������� ���� ���� �������� ���� -> ����������.
 * Q. ���ÿ� �ִ� ��� �� ���ֿ� ���� ���� ���� ���� ���� �շ� �� �ִ밪 -> �ּ� ���� Ʈ�� 
 *     -> result = all total - kruskal - total
 * 
 * 
 * 
 * */

public class backjoon_6497 {

	// ���� ���� �� 
	static int[] parent;
	static ArrayList<lightCity> nodes;
	static int total;
	static boolean inputCheck;
	
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
		total = 0;
		parent = new int[m + 1];
		
		for(int i = 1; i <= m; i++) {
			parent[i] = i;
		}

		Collections.sort(nodes);
		int result = 0;
		
		
		for(lightCity city : nodes) {
			lightCity cityNode = city;
			
			if(find(cityNode.fristLigth) != find(cityNode.endLight)) {
				union(cityNode.fristLigth, cityNode.endLight);
				result += cityNode.result;
				
			}
		}
		int answer = total - result;
		return answer;
	}
	
	
	// ����
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer stringTk;
		nodes = new ArrayList<lightCity>();
			
		while(inputCheck == false) {
			stringTk = new StringTokenizer(reader.readLine());
			int m = Integer.parseInt(stringTk.nextToken());
			int n = Integer.parseInt(stringTk.nextToken());
			
			if(n == 0 && m == 0) {
				inputCheck = true;
				break;
			}
			else inputCheck = false;
			
			for(int i = 0; i < n; i++) {
				stringTk = new StringTokenizer(reader.readLine());
				int x = Integer.parseInt(stringTk.nextToken());
				int y = Integer.parseInt(stringTk.nextToken());
				int z = Integer.parseInt(stringTk.nextToken());	
				total += z;
				nodes.add(new lightCity(x, y, z));
			}
			
			int result = kruskal(m);
			writer.write(result + "\n");
			writer.flush();
			nodes = new ArrayList<lightCity>();
			
		}
		writer.close();
		reader.close();
	}
	
}

class lightCity implements Comparable<lightCity>{

	int fristLigth;
	int endLight;
	int result;
	
	public lightCity(int fristLight, int endLight, int result) {
		this.fristLigth = fristLight;
		this.endLight = endLight;
		this.result = result;
	}
	
	@Override
	public int compareTo(lightCity o) {
		if(result < o.result) return -1;
		else return 1;
	}
}


