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


/**
 * [��������]
 * �׷����� ��尡 �Ž����� �ʰ� ����Ǿ��ִ� �׷����� �ǵ��� �����ϴ� ����� ���� 
 * DAG���� ������ ������ ���Ĺ��
 * ���� : ������ ������ ������ ����(����Ŭ�� �߻��ϸ� �ȵ�)
 * ��� : Stack / Queue 2������ ��� ���� 
 * �ַ� ����ϴ� ��� : Queue ���
 * 				-> 2���� �迭�� ��� 
 * 
 * ex) ����� �׷����� 3 - 1, 3 - 2 ��� �����ϸ�
 * 3�� 1�� 2�� ����Ǿ� �ֱ� ������ 2���� ��������(������ ����)�� ������
 * 1�� 2�� 0���� ���������� ������. 
 * �׷��� ������ �������Ŀ� ������ ���������� 0�� ģ������� �����ϰ� ���������� 0�̻��� ��� 0���� �ϳ��� ���ָ鼭 ����ϸ� �ȴ�.
 * 
 * >> ����
 * scanner���� ����� �ӵ��� ���� BufferedReader�� BufferedWriter�� ������� �޴´�. 
 * StringTokenizer�� �̿��Ͽ� ���ڿ��� ������ üũ
 * 
 * >> ���� 
 * degree : ���������� ���� �����迭 
 * sortList : �Է¹��� ������ ������踦 ��Ÿ���� ���� ���� ArrayList
 * lNum�� rNum : n�� m��
 * 
 * */

// �������Ŀ��� DFS ��ĺ��� Qeueu�� ���� ���� ȿ���� 
public class backjoon_2252 {
	static int n;
	static int m;

	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st;
		st = new StringTokenizer(reader.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		int[] degree = new int[n];
		ArrayList<ArrayList<Integer>> sortList = new ArrayList<>();
		
		for(int i = 0; i < n; i++) {
			sortList.add(new ArrayList<Integer>()); 
		}
		
		// �����ϴ� ���� �������� sortList�� degree�� ǥ�����ش�. 
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(reader.readLine());
			int lNum = Integer.parseInt(st.nextToken());
			int rNum = Integer.parseInt(st.nextToken());
			sortList.get(lNum-1).add(rNum-1);
			degree[rNum-1]++;
		}

	
		Queue<Integer> queue = new LinkedList<Integer>();
		Queue<Integer> result = new LinkedList<Integer>();
		
		
		// �ڽ��� ����Ű�� �ִ°��� ���ٸ� ���������� 0�̱� ������ queue�� �߰��Ѵ�.
		for(int i = 0; i < n; i++) {
			if(degree[i] == 0) {
				queue.add(i);
			}
		}
		
		int current;
		while(!queue.isEmpty()) {
			// �ϳ��� ��� ť�� ���� �����鼭 ����� ������ Ž���ϰ� ���������� 0�̵Ǹ� �����ϰ� Queue�� ���´�. 
			current = queue.poll();
			result.add(current);
			
			for(int i : sortList.get(current)) {
				degree[i]--;
				
				if(degree[i]==0) {
					queue.add(i);
				}
				
			}
			
		}
	
		while(!result.isEmpty()) {
			writer.write((result.poll() + 1) + " ");
		}
		
		writer.flush();
		writer.close();
	}
}