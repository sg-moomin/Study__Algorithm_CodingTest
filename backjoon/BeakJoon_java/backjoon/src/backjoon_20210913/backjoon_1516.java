package backjoon_20210913;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

import javafx.scene.chart.ValueAxis;

/**
 * [백준-1516]
 * 예를 들어서 짜장면(5)과 돈까스집(5) 그리고 고기집(4) 3개를 순서대로 지을 때 
 * 건물 번호는 돈까스집이 1번, 고기집이 1번, 짜장면집은 없다고 가정하면
 * 짜장면집은 순서가 없기 때문에 5만큼의 시간이 걸린다. 그렇지만 돈까스와 고기집의 경우에는 짜장면집이 지어진 뒤에 
 * 지을 수 있기 때문에 각각 4+5, 5+5의 여유값이 필요하다.
 * 만약 고깃집이 건물번호가 1번, 2번이라고 한다면 (4+5)+5만큼의 여유 시간이 필요하게 된다
 * 즉 하나의 건물을 지을 때 그리고 건물번호가 존재한다면 해당 건물번호에 해당하는 시간만큼 넉넉하게 잡아서 계산해야 하는것이 포인트다.
 * 문제 요점 : 해당 순번에 대한 건물을 짓는데 최대 시간을 측정한다.
 * 
 * 이번문제도 동일하게 위상정렬을 이용하여 풀 수 있다.
 * 위상정렬 요점 : 순서가 정해진 정렬을 말함(사이클이 발생하면 안됨)
 * 
 * 
 * >> 변수 
 * degree : 진입차수를 위한 정수배열 
 * sortList : 입력받은 노드들의 연결관계를 나타내기 위한 정수 ArrayList
 * indexValue : 값을 담기 위한 정수배열
 * currentValue : 건물번호까지 합친 값을 담기위한 정수배열
 * 
 * */

public class backjoon_1516 {

	public static void main(String[] args) throws IOException {
		
		//
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st;
		int n = Integer.parseInt(reader.readLine());

		int[] degree = new int[n+1];
		int[] indexValue = new int[n+1];
		int[] currentValue = new int[n+1];
		ArrayList<ArrayList<Integer>> sortList = new ArrayList<>();
//		ArrayList<Integer> sortList = new ArrayList[n+1];
		
		for(int i = 1; i <= n+1; i++) {
//			sortList[i] = new ArrayList<Integer>()
			sortList.add(new ArrayList<Integer>()); 
		}
		
		
		for(int i = 1; i <= n; i++) {
			st = new StringTokenizer(reader.readLine());
			indexValue[i] = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			while(m != -1) {
				degree[i]++;
				sortList.get(m).add(i);
				m = Integer.parseInt(st.nextToken());
			}
		}
		
	
		Queue<Integer> queue = new LinkedList<Integer>();
		Queue<Integer> result = new LinkedList<Integer>();
		
		
		for(int i = 1; i <= n; i++) {
			if(degree[i] == 0) {
				queue.add(i);
				currentValue[i] = indexValue[i];
			}
		}
		
//		int current;

		while(!queue.isEmpty()) {
			int num = queue.poll();
			for(int i : sortList.get(num)) {
				degree[i]--;
				currentValue[i] = Math.max(currentValue[i], currentValue[num] + indexValue[i]);
				if(degree[i] == 0) {
					queue.offer(i);
				}
			}
			
		}
		
		
		
		for(int i = 1; i < currentValue.length; i++) {
			writer.write(currentValue[i] + "\n");
		}
		
		writer.flush();
		writer.close();
		
	}	
	
	
//	ArrayList<ArrayList<Integer>> sortList = new ArrayList<>();
}
