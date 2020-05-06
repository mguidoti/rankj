import sys

results = {}

if sys.argv[1] == "nsp":
    in_filename = "results\\WoS_nsp_final.txt"
    out_filename = "results\\nsp_out.csv"
    print(in_filename)
    print(out_filename)
elif sys.argv[1] == "newTaxa":
    in_filename = "results\\WoS_newTaxa_final.txt"
    out_filename = "results\\newTaxa_out.csv"
    print(in_filename)
    print(out_filename)
elif sys.argv[1] == "nomenActs":
    in_filename = "results\\WoS_nomenActs_final.txt"
    out_filename = "results\\nomenActs_out.csv"
    print(in_filename)
    print(out_filename)
else:
    print("Please, specify a correct parameter.")

with open(in_filename, encoding='utf-8') as in_file, open(out_filename, 'w') as out_file:
    for line in in_file:
        if line[0:2] == "SO":
            if line[3:][:-1] in results.keys():
                results[line[3:][:-1]] += 1
            else:
                results[line[3:][:-1]] = 1

    results_sorted = sorted(results.items(), key=lambda x: x[1], reverse=True)

    total_papers = 0

    for each in results_sorted:
        total_papers += each[1]

    out_file.write("Journal;Papers;Proportion;Accumulated\n")

    accumulation = 0

    for each in results_sorted:
        accumulation += each[1]/total_papers*100
        processed_line = each[0] + ";" + str(each[1]) + ";" + str(each[1]/total_papers*100) + ";" + str(accumulation) + "\n"
        out_file.write(processed_line)