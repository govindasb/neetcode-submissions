class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> map = new HashMap<>();
        for(String s: strs){
            char[] temp = s.toCharArray();
            Arrays.sort(temp);
            String t = new String(temp); 
            if(map.containsKey(t)){
                map.get(t).add(s);
            }
            else{
                List<String> newList = new ArrayList<>();
                newList.add(s);
                map.put(t, newList);
            }
        }
        return new ArrayList<>(map.values());
    }
}
