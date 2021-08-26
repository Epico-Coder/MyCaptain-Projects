def set_operations(set1: set, set2: set):
  union = set1.union(set2)
  intersection = set1.intersection(set2)
  difference1 = set1.difference(set2)
  difference2 = set2.difference(set1)
  sym_difference = set1.symmetric_difference(set2)

  return f"Union of Set 1 and Set 2: {union}\n" \
         f"Intersection of Set 1 and Set 2: {intersection}\n" \
         f"Difference of Set 1 from Set 2: {difference1}\n" \
         f"Difference of Set 2 from Set 1: {difference2}\n" \
         f"Symmetrical Difference of Set 1 and Set 2: {sym_difference}"
