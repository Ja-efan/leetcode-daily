# LeetCode Daily Log

> 목표: 1일 1문제 + 복기(Takeaways) + 필요시 Revisit  
> 규칙: 하루 최소 1문제 / 커밋: `<state>: LC-<id> <title> [D]`

---

## Stats
- Start date: 2026-01-12
- Restart date: 2026-11-01 (2026-02-02 이후 공백 후 재시작)
- Current streak: 3
- Total solved: 21 (E:14 / M:7 / H:0)

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
| 11/04 (수) | Sliding Window | 121 Best Time to Buy and Sell Stock (E) | 3 Longest Substring Without Repeating Characters (M) | [ ] |
| 11/05 (목) | Binary Search | 704 Binary Search (E) | 875 Koko Eating Bananas (M) | [ ] |
| 11/06 (금) | BFS / DFS (Grid) | 200 Number of Islands (M) | 994 Rotting Oranges (M) | [ ] |
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



**Legend**
- Result:  
  - Accepted: `AC`  
  - Time Limit Exceeded: `TLE`
  - Wrong Answer: `WA`
  - Runtime Error: `RE`
  - Do Not Finish: `DNF`  
  
- Topics 예시: `HashMap`, `Two Pointers`, `Sliding Window`, `Binary Search`, `DP`, `Graph`, `Tree`, `Greedy`, etc.

---