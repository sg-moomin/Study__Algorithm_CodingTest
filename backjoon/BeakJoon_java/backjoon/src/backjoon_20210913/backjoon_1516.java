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
 * [����-1516]
 * ���� �� ¥���(5)�� �����(5) �׸��� ������(4) 3���� ������� ���� �� 
 * �ǹ� ��ȣ�� ������� 1��, �������� 1��, ¥������� ���ٰ� �����ϸ�
 * ¥������� ������ ���� ������ 5��ŭ�� �ð��� �ɸ���. �׷����� ����� �������� ��쿡�� ¥������� ������ �ڿ� 
 * ���� �� �ֱ� ������ ���� 4+5, 5+5�� �������� �ʿ��ϴ�.
 * ���� �������� �ǹ���ȣ�� 1��, 2���̶�� �Ѵٸ� (4+5)+5��ŭ�� ���� �ð��� �ʿ��ϰ� �ȴ�
 * �� �ϳ��� �ǹ��� ���� �� �׸��� �ǹ���ȣ�� �����Ѵٸ� �ش� �ǹ���ȣ�� �ش��ϴ� �ð���ŭ �˳��ϰ� ��Ƽ� ����ؾ� �ϴ°��� ����Ʈ��.
 * ���� ���� : �ش� ������ ���� �ǹ��� ���µ� �ִ� �ð��� �����Ѵ�.
 * 
 * �̹������� �����ϰ� ���������� �̿��Ͽ� Ǯ �� �ִ�.
 * �������� ���� : ������ ������ ������ ����(����Ŭ�� �߻��ϸ� �ȵ�)
 * 
 * 
 * >> ���� 
 * degree : ���������� ���� �����迭 
 * sortList : �Է¹��� ������ ������踦 ��Ÿ���� ���� ���� ArrayList
 * indexValue : ���� ��� ���� �����迭
 * currentValue : �ǹ���ȣ���� ��ģ ���� ������� �����迭
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