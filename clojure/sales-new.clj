(require ['clojure.string :as 'str])

(defn get-lines [file]
  (map #(str/split % #"\|") (str/split-lines (slurp file))))

(def customer (map #(hash-map (keyword (first %1)) (vec (rest %1))) (get-lines "cust.txt")))

(def cust (apply merge customer))

(def sorted-cust (into (sorted-map) cust))

(def product (map #(hash-map (keyword (first %1)) (vec (rest %1))) (get-lines "prod.txt")))

(def prod (apply merge product))

(def sorted-prod (into (sorted-map) prod))

(def sales (map #(hash-map (keyword (first %1)) (vec (rest %1))) (get-lines "sales.txt")))

(def sale (apply merge sales))

(def sorted-sale (into (sorted-map) sale))

(defn cc [yyc]
  (first (reduce-kv (fn [acc k v]
     (if (= (get v 0) (str yyc))
       (conj acc k)
       acc))
     #{} sorted-prod)))

(defn ccc [yyc]
  (first (reduce-kv (fn [acc k v]
     (if (= (get v 0) (str yyc))
       (conj acc k)
       acc))
     #{} sorted-cust)))
    
(defn cccc [yyc]
  (first (reduce-kv (fn [acc k v]
     (if (= (name k) (str yyc))
       (conj acc (get v 1))
       acc))
     #{} sorted-prod)))

(let [m (.getDeclaredMethod clojure.lang.LispReader
                            "matchNumber"
                            (into-array [String]))]
  (.setAccessible m true)
  (defn parse-number [s]
    (.invoke m clojure.lang.LispReader (into-array [s]))))

(defn option-one []
    (doseq [[k v] sorted-cust] (prn (name k) v)))

(defn option-two []
  (doseq [[k v] sorted-prod] (prn (name k) v)))

(defn option-three []
  (doseq [[k v] sorted-sale] 
    (let [first (get v 0) second (get v 1) third (get v 2)]
    (prn (name k) (get (get sorted-cust (keyword first)) 0) (get (get sorted-prod (keyword second)) 0) third))))

(defn option-four []
  (println "Enter a Customer name?")
  (let [yyinput (read-line)]
    (let [check (ccc yyinput)]
      (if (nil? check) (println "Customer doesn't Exist") (println yyinput ":" (reduce + (into [] (reduce-kv (fn [acc k v]
        (if (= (get v 0) (str (name (ccc yyinput))))
          (conj acc (* (parse-number (cccc (str (get v 1)))) (parse-number (get v 2))))
          acc))
        #{} sorted-sale))))))))

(defn option-five []
  (println "Enter a product name?")
  (let [input (read-line) yyinput (read-string input)]
    (let [check (cc yyinput)]
      (if (nil? check) (println "Product doesn't exist") (println yyinput ":" (reduce + (into [] (reduce-kv (fn [acc k v]
        (if (= (get v 1) (str (name (cc yyinput))))
          (conj acc (Integer/parseInt (get v 2)))
          acc))
        #{} sorted-sale))))))))

(defn option-six []
  (println "Good Bye!")
  (System/exit 0))

(defn main []
  (println "*** Sales Menu ***")
  (println "------------------")
  (println "1. Display Customer Table")
  (println "2. Display Product Table")
  (println "3. Display Sales Table")
  (println "4. Total Sales for Customer")
  (println "5. Total Count for Product")
  (println "6. Exit")
  (println "")
  (println "Enter an option?")
  (let [input (read-line) yyinput (read-string input)]
    (case yyinput
      1 (option-one)
      2 (option-two)
      3 (option-three)
      4 (option-four)
      5 (option-five)
      6 (option-six))))

(main)



