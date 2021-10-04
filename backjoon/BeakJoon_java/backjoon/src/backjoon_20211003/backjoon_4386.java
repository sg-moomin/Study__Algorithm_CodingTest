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
 * [별자리 만들기]
 * Q.별자리를 이루는 선은 서로 다른 두별을 일직선으로 이은 형태이다 -> 2개의 정점을 1개의 간선으로 이어준다.
 * Q.모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다. -> 1-2 / 2-3 => 1-3 
 * A. 피타고라스 정리를 사용하면 됨 
 * */

public class backjoon_4386 {
	static int[] parent;
	static ArrayList<starNode> nodeList;
	static ArrayList<stars> checkList;
	
	
	// 피타고라스 정의 이용
	public static double Pythagoras(stars s1, stars s2) {
		double x = s1.frist - s2.frist;
		double y = s1.end - s2.end;
		return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
	}
	
	
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
	
	public static double kruskal(int numbers) {
		parent = new int[numbers + 1];
	
		for(int i = 1; i <= numbers; i++) {
			parent[i] = i;
		}
		
		Collections.sort(nodeList);
		
		double answer = 0;
		for(starNode star : nodeList){
			starNode nodes = star;

			if(find(nodes.fristStar) != find(nodes.endStar)){
				answer += nodes.result; 
				union(nodes.fristStar, nodes.endStar);
			}
			
		}
		
		// 소숫점 2자리
		double result = Double.parseDouble(String.format("%.2f", answer));
		return result;
	}
	
	public static void main(String args[]) throws IOException {
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer stringTk;
		
		int numbers = Integer.parseInt(reader.readLine());
		nodeList = new ArrayList<starNode>();
		checkList = new ArrayList<stars>();
		
		for(int i = 0; i < numbers; i++) {
			stringTk = new StringTokenizer(reader.readLine());
			double fristPoint = Double.parseDouble(stringTk.nextToken());
			double endPoint = Double.parseDouble(stringTk.nextToken());
			
			checkList.add(new stars(i, fristPoint, endPoint));
		}
		
		
		for(int i = 0; i < numbers; i++) {
			for (int j = i + 1; j < numbers; j++) {
				double nums = Pythagoras(checkList.get(i), checkList.get(j));
				
				nodeList.add(new starNode(checkList.get(i).n, checkList.get(j).n, nums));
			}
		}
		
		double result = kruskal(numbers);
		
		writer.write(result + "\n");
		writer.flush();
		writer.close();
		reader.close();
		
		
	}
}


class stars {
	int n;
	double frist;
	double end;
	
	stars(int n, double frist, double end){
		this.end = end;
		this.frist = frist;
		this.n = n;
	}
	
}

class starNode implements Comparable<starNode>{
	int fristStar;
	int endStar;
	double result;
	
	starNode(int fristStar, int endStar, double result){
		this.fristStar = fristStar;
		this.endStar = endStar;
		this.result = result;
	}

	@Override
	public int compareTo(starNode star) {
		// 오름차순	
		if(result < star.result) return -1;
		else return 1;
	}
}

