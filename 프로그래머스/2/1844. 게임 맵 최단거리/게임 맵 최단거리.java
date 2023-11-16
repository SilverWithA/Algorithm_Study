import java.util.*;

class Solution {
    // 움직일 방위 정보 - leftRight, upDown
    static final int[] leftRight = new int[]{1, -1, 0, 0},
                        upDown = new int[]{0, 0, 1, -1};
    
    // 위치 정보 및 움직인 거리 정보 관리 - Node 클래스
    static class Node{
        final int x;
        final int y;
        final int moveCount;
        
        // 게이머 위치 업데이트를 위한 생성자
        public Node(int x, int y, int moveCount){
            this.x = x;
            this.y = y;
            this.moveCount = moveCount;
        }
    }
    
    public int solution(int[][] maps) {
        // n x m 크기의 maps 정보 저장
        int n = maps.length;
        int m = maps[0].length;
        
        // 이미 방문한 경로 and 막힌 구간 정보 관리 - visited
        boolean[][] visited = new boolean[n][m];
        
        // 막힌 구간 정보 visited에 저장
        for(int i = 0; i < maps.length; i++){
            for(int j = 0; j < maps[i].length; j++){
                if(maps[i][j] == 0){
                    visited[i][j] = true;
                }
            }
        }
        
        // 최단 거리 탐색 시작 ------------------------------------
        Queue<Node> playerLocation = new LinkedList<>();
        // 시작 위치 방문 정보 및 
        visited[0][0] = true;
        playerLocation.offer(new Node(0, 0, 1));
        int answer = 0;
        
        while(!playerLocation.isEmpty()){
            
            Node node = playerLocation.poll();
            // 4방위에 대해 이동 가능 여부를 판단하여 이동
            for(int i = 0; i < 4; i++){
                // 4방위의 모든 이동 경우의 수
                int routeRow = node.x + leftRight[i];
                int routeCol = node.y + upDown[i];
                
                // 이동할 수 없는 경우 - 지도 밖의 경우
                if (n <= routeRow || routeRow < 0 || m <= routeCol || routeCol < 0){
                    continue;
                }
                // 막힌 길이거나 이미 방문한 경우
                if(visited[routeRow][routeCol]){
                    continue;
                }
                
                // 방문 기록 저장
                visited[routeRow][routeCol] = true;
                // 위치 이동
                playerLocation.add(new Node(routeRow, routeCol, node.moveCount + 1));
                
                // 최종 도착지점에 도착했을때 이동 거리 저장
                if(routeRow == n - 1 && routeCol == m - 1){
                    answer = node.moveCount + 1;
                }
            }
        }
        return answer == 0 ? -1 : answer;
    }
}