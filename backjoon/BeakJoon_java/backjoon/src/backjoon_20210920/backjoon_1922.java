package backjoon_20210920;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.Collections;

/** 
 * [Kruskal-MST]
* 최소 비용 신장 트리가 최소 비용의 간선을 선택하는 그래프
* 조건은 사이클이 생성되면 안된다는 조건은 필수이다.
* 따라서 사이클이 생성되어 있는지 여부를 확인해야 하는데 이는 union-find 알고리즘으로 확인한다.
* 
* [union find]
* 서로소 집합 자료 구조라 한다.
* 원소 x와 원소 y가 속해있는 집합을 입력받아서 합집합(union)을 만들어 준다. 
* 합친 결과에서 find(x)를 할 경우 x가 속한 집합을 반환해주면 된다.
* 
* 
* [Kruskal-MST 알고리즘 사용 이유]
* 탐욕 방법 중 하나로 가장 짧은 노드를 선택하여 최종적인 해답에 도달하는 방법 중 하나이다.
* 당시에 최적이라고 생각했으나 결과가 최적이라는 건 보장할 수 없다.
* 그래서 Kruskal를 이용하여 검증하고 최적의 해답을 찾으면 된다.
* 
*
*
*
**/

class Nodes implements Comparable<Nodes> {
	int start;
	int end;
	int result;

	Nodes(int start, int end, int result) {
		this.start = start;
		this.end = end;
		this.result = result;
	}

	@Override
	public int compareTo(Nodes o) {
		return result - o.result;
	}

}

public class backjoon_1922{

	static ArrayList<Nodes> nodeList;
	static int[] parent;

	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer StringToken;

		int N = Integer.parseInt(reader.readLine());
		int M = Integer.parseInt(reader.readLine());
		
		nodeList = new ArrayList<>();

		
		for(int i = 0; i < M; i++){
			StringToken = new StringTokenizer(reader.readLine());
			int start = Integer.parseInt(StringToken.nextToken());
			int end = Integer.parseInt(StringToken.nextToken());
			int result  = Integer.parseInt(StringToken.nextToken());

			
			
			nodeList.add(new Nodes(start, end, result));
		}

		parent = new int[N + 1];
		for(int i = 1; i <= N; i++){
			parent[i] = i;
		}

		
		Collections.sort(nodeList);
	

		int answer = 0;
		for (Nodes lists : nodeList){
			Nodes node = lists;
			// System.out.print("node입니다. : " + node.start + " " + node.end + " " + node.result + " ");
			// System.out.print("findX. : " + find(node.start));
			// System.out.println("findY. : " + find(node.end));
			
			if(find(node.start) != find(node.end)){
				answer += node.result;
				union(node.start, node.end);
			}
			
		}
		
		writer.write(answer + "\n");
		writer.flush();
		writer.close();
		reader.close();
		
	}

	public static int find(int answer){
		if (parent[answer] == answer){
			return answer;
		} 
		else{
			return parent[answer] = find(parent[answer]);
		}
	}
	
	//
	public static void union(int x, int y){
		x = find(x);
		y = find(y);

		// 동일하지 않을 경우 확인
		if(x != y){
			parent[y] = x;
		}
	} 
}