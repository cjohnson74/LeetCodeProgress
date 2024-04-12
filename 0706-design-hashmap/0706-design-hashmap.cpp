#include <vector>
using namespace std;

class MyHashMap {
private:
    vector<int> internal_map;
public:
    MyHashMap() {
        internal_map.resize(10e6);
        fill(internal_map.begin(), internal_map.end(), -1);
    }
    
    void put(int key, int value) {
        internal_map[key] = value;
    }
    
    int get(int key) {
        return internal_map[key];
    }
    
    void remove(int key) {
        internal_map[key] = -1;
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */