# LeetCode Daily Log

> 목표: 1일 1문제 + 복기(Takeaways) + 필요시 Revisit  
> 규칙: 하루 최소 1문제 / 커밋: `<state>: LC-<id> <title> [D]`

---

## Stats
- Start date: 2026-01-12
- Restart date: 2026-11-01 (2026-02-02 이후 공백 후 재시작)
- Current streak: 19
- Total solved: 43 (E:27 / M:16 / H:0)

---

## Weekly Plan

### Week 1 (2026-11-01 ~ 2026-11-08) · 코테 기본 패턴
- 목표: 8일 연속 커밋 / 필수 8문제 / `notes/patterns.md` 패턴 6개 정리
- 시간 제한: Easy 20분, Medium 40분. 넘기면 힌트·풀이 확인 후 `notes/revisit.md`에 등록

| Date | Topic | Must | Stretch | Done |
|---|---|---|---|:---:|
| 11/01 (일) | 재정비 + 워밍업 | 217 Contains Duplicate (E) | - | [x] |
| 11/02 (월) | HashMap | 242 Valid Anagram (E) | 49 Group Anagrams (M) | [x] |
| 11/03 (화) | Two Pointers | 167 Two Sum II - Input Array Is Sorted (M) | 15 3Sum (M) | [x] |
| 11/04 (수) | Sliding Window | 121 Best Time to Buy and Sell Stock (E) | 3 Longest Substring Without Repeating Characters (M) | [x] |
| 11/05 (목) | Binary Search | 704 Binary Search (E) | 875 Koko Eating Bananas (M) | [ ] |
| 11/06 (금) | BFS / DFS (Grid) | 200 Number of Islands (M) | 994 Rotting Oranges (M) | [x] |
| 11/07 (토) | Heap / Top-K | 1046 Last Stone Weight (E) | 347 Top K Frequent Elements (M) | [ ] |
| 11/08 (일) | Review + 실전 | Revisit 645, 636 재풀이 | 739 Daily Temperatures (M, 40분 타이머) | [ ] |

---

## Daily Log

| Date | LC ID | Title | Difficulty | Lang | Time Spent | Result | Topics | Takeaways (1-liner) |
|---|---:|---|---|---|---:|---|---|---|
| 2026-01-12 | 1929 | Concatenation of Array  | Easy | Python | 1 min | `AC` | `Array` | 리스트 끼리의 + 연산은 새로운 리스트를 만든다. | 
| 2026-01-13 | 1470 | Shuffle the Array  | Easy | Python | 1 min | `AC` | `Array` | 리스트 슬라이싱은 새로운 메모리를 메모리에 할당한다. |
| 2026-01-14 | 645 | Set Mismatch | Easy | Python | 20 min | `AC` | `Array` | 더 효율적인 방법을 고안해본다. (for 문 한 번 순회) |
| 2026-01-15 | 1365 | How Many Numbers Are Smaller Than the Current Number  | Easy | Python | 20 min | `AC` | `Array` | - |
| 2026-01-16 | 448 | Find All Numbers Disappeared in an Array | Easy | Python | 5 min | `AC` | `Array` | - |
| 2026-01-17 | - |  |  |  |  |  |  |  |
| 2026-01-18 | 1441 | Build an Array With Stack Operations | Medium | Python | 10 min | `AC` | `Stack` | - |
| 2026-01-19 | 150 | Evaluate Reverse Polish Notation | Medium | Python | 15 min | `AC` | `Stack` | - |
| 2026-01-20 | 636 | Exclusive Time of Functions | Medium | Python | 30 min | `AC` | `Stack` | - |
| 2026-01-21 | 1475 | Final Prices With a Special Discount in a Shop | Easy | Python | 15 min | `AC` | `Stack` | - |
| 2026-01-22 | 1 | Two Sum | Easy | Python | 1 min | `AC` | `Brute Force` | - |
| 2026-01-24 | 2 | Add Two Numbers | Medium | Python | 20 min | `AC` | `pointer` | - |
| 2026-01-25 | 9 | Palindrome Number | Easy | Python | 1 min | `AC` | `string` | - |
| 2026-01-26 | 13 | Roman to Integer | Easy | Python | 10 min | `AC` | `hashmap` | - |
| 2026-01-27 | 14 | Longest Common Prefix | Easy | Python | 10 min | `AC` | `Brute Force` | - |
| 2026-01-28 | 20 | Valid Parentheses | Easy | Python | 5 min | `AC` | `Stack` | - |
| 2026-02-02 | 21 | Merge Two Sorted Lists | Easy | Python | 10 min | `AC` | `Linked List` | - |
| 2026-11-01 | 217 | Contains Duplicate | Easy | Python | 5 min | `AC` | `HashMap` `Set` | 중복 체크는 set 멤버십(O(1)), 순회하면 중복 발견 즉시 종료 가능 |
| 2026-11-02 | 242 | Valid Anagram | Easy | Python | 5 min | `AC` | `HashMap` `Sorting` | 정렬은 O(N log N), Counter 비교는 O(N). Counter == 는 키와 개수가 모두 같은지 비교 |
| 2026-11-02 | 49 | Group Anagrams | Medium | Python | 10 min | `AC` | `HashMap` `Sorting` | 정규화한 값(정렬 문자열)을 key로 묶는다. 개수 튜플 key면 O(N*K) |
| 2026-11-03 | 167 | Two Sum II - Input Array Is Sorted | Medium | Python | 15 min | `AC` | `Two Pointers` | 정렬된 배열에서 합 찾기는 양 끝 두 포인터로 O(N) |
| 2026-11-03 | 15 | 3Sum | Medium | Python | 30 min | `AC` | `Two Pointers` `Sorting` | 정렬 후 한 값을 고정하고 두 포인터로 탐색하면 O(N^2) |
| 2026-11-04 | 121 | Best Time to Buy and Sell Stock | Easy | Python | 5 min | `AC` | `Array` `Sliding Window` | 최저가를 들고 한 번 순회하면 O(N) |
| 2026-11-05 | 704 | Binary Search | Easy | Python | - | `AC` | `Binary Search` | - |
| 2026-11-06 | 200 | Number of Islands | Medium | Python | 20 min | `AC` | `BFS` `Matrix` | 탐색을 새로 시작하는 횟수가 섬의 개수 |
| 2026-11-09 | 1046 | Last Stone Weight | Easy | Python | 10 min | `AC` | `Heap` | 최대 힙은 부호를 뒤집은 최소 힙으로 구현 |
| 2026-11-09 | 1 | Two Sum (복습) | Easy | Python | 30 min | `AC` | `HashMap` | 복습: 해시맵 조회로 O(N) |
| 2026-11-10 | 206 | Reverse Linked List | Easy | Python | - | `AC` | `Linked List` | 값이 아니라 next 화살표 방향을 뒤집는다 |
| 2026-11-10 | 645 | Set Mismatch (복습) | Easy | Python | - | `AC` | `HashMap` `Set` | 복습: set 으로 중복과 누락을 각각 찾는다 |
| 2026-11-11 | 155 | Min Stack | Medium | Python | 20 min | `AC` | `Stack` | 넣을 때 그 시점의 최솟값을 함께 저장하면 getMin O(1) |
| 2026-11-12 | 104 | Maximum Depth of Binary Tree | Easy | Python | - | `AC` | `Tree` `BFS/DFS` | 스택 두 개로 층 단위 탐색하며 층 수를 센다 |
| 2026-11-13 | 102 | Binary Tree Level Order Traversal | Medium | Python | - | `AC` | `Tree` `BFS/DFS` | 순서를 지켜야 하면 큐(deque.popleft)로 층 단위 탐색 |
| 2026-11-14 | 70 | Climbing Stairs | Easy | Python | 10 min | `AC` | `DP` | 점화식 s(n) = s(n-1) + s(n-2) 로 DP 테이블을 채운다 |
| 2026-11-15 | 746 | Min Cost Climbing Stairs | Easy | Python | - | `AC` | `DP` | 점화식에 비용을 더해 최소 비용 DP 테이블을 채운다 |
| 2026-11-16 | 141 | Linked List Cycle | Easy | Python | 15 min | `AC` | `Linked List` `Two Pointers` | 속도가 다른 두 포인터로 사이클을 O(1) 공간에 찾는다 |
| 2026-11-17 | 733 | Flood Fill | Easy | Python | 20 min | `AC` | `BFS/DFS` `Matrix` | 칠하는 것이 방문 표시를 대신한다 |
| 2026-11-18 | 1971 | Find if Path Exists in Graph | Easy | Python | 10 min | `AC` | `BFS/DFS` `Graph` | 인접 리스트와 스택 DFS로 source에서 갈 수 있는 노드를 탐색한다 |
| 2026-11-19 | 78 | Subsets | Medium | Python | 15 min | `AC` | `Backtracking` | itertools.combinations로 크기별 조합을 만들어 모든 부분집합을 구했다 |
| 2026-11-20 | 17 | Letter Combinations of a Phone Number | Medium | Python | 30 min | `AC` | `Backtracking` | 자리마다 후보 글자를 붙이며 재귀 호출하고, 길이가 digits 길이와 같아지면 결과에 추가한다 |
| 2026-11-21 | 125 | Valid Palindrome | Easy | Python | 15 min | `AC` | `Two Pointers` `String` | 영숫자만 남긴 문자열을 양 끝 두 포인터로 비교한다 |
| 2026-11-22 | 136 | Single Number | Easy | Python | 30 min | `AC` | `Array` `Bit Manipulation` | 모든 원소를 XOR로 누적해 짝을 지우고 남은 값을 반환했다 |
| 2026-11-23 | 543 | Diameter of Binary Tree | Easy | Python | 20 min | `AC` | `Tree` `DFS` | 높이를 반환하며 노드마다 left + right 로 지름을 갱신했다 |
| 2026-11-24 | 56 | Merge Intervals | Medium | Python | 15 min | `AC` | `Array` `Sorting` | 시작점 기준으로 정렬한 뒤 마지막 병합 구간의 end 와 비교해 병합했다 |
| 2026-11-25 | 33 | Search in Rotated Sorted Array | Medium | Python | 30 min | `AC` | `Binary Search` `Array` | 정렬된 쪽을 먼저 판별한 뒤 그 구간 안에 target 이 있는지로 탐색 범위를 좁혔다 |
| 2026-11-26 | 322 | Coin Change | Medium | Python | 20 min | `AC` | `DP` | 마지막 동전을 고정하고 dp[i - coin] + 1 의 최솟값으로 dp 테이블을 채웠다 |
| 2026-11-27 | 207 | Course Schedule | Medium | Python | 30 min | `AC` | `Graph` `BFS/DFS` | 선수과목 수가 0인 과목부터 들으며 후속과목의 수를 줄이고, 들은 과목 수를 전체와 비교했다 |



**Legend**
- Result:  
  - Accepted: `AC`  
  - Time Limit Exceeded: `TLE`
  - Wrong Answer: `WA`
  - Runtime Error: `RE`
  - Do Not Finish: `DNF`  
  
- Topics 예시: `HashMap`, `Two Pointers`, `Sliding Window`, `Binary Search`, `DP`, `Graph`, `Tree`, `Greedy`, etc.

---