import random
# This challenge is about Biology.

# so i didnt get the exactly answer, but i got to create the number for an entire chromosome line
# to be all 1





class Genes():
    def __init__(self):
        self.value = random.choice([True, False])

    def mutate(self):
        self.value = random.choice([True, False])


genp = Genes()
genp.mutate()
print(genp.value)



class Chromosome():
    def __init__(self, gen1, gen2, gen3, gen4, gen5, gen6, gen7, gen8, gen9, gen10):
        self.list_of_gens = [gen1, gen2, gen3, gen4, gen5, gen6, gen7, gen8, gen9, gen10]
        self.gen1_value = gen1.value
        self.gen2_value = gen2.value
        self.gen3_value = gen3.value
        self.gen4_value = gen4.value
        self.gen5_value = gen5.value
        self.gen6_value = gen6.value
        self.gen7_value = gen7.value
        self.gen8_value = gen8.value
        self.gen9_value = gen9.value
        self.gen10_value = gen10.value
        self.all_trues = False
        self.ietations = 0
    # def print_chrom(self):
    #     print(f"{self.gen1_value}, {self.gen2_value}, {self.gen3_value}, {self.gen4_value}, {self.gen5_value}, {self.gen6_value}, {self.gen7_value}, {self.gen8_value}, {self.gen9_value}, {self.gen10_value}")
    
    def mutate(self):
        for gene in self.list_of_gens:
            if random.choice([True, False]):
                gene.mutate()
        # print(self.list_of_gens)
        # print(f"{self.gen1_value}, {self.gen2_value}, {self.gen3_value}, {self.gen4_value}, {self.gen5_value}, {self.gen6_value}, {self.gen7_value}, {self.gen8_value}, {self.gen9_value}, {self.gen10_value}")


    def all_true_chrom(self):
        while not self.all_trues:
            self.mutate()
            self.ietations += 1
            all_bools = []
            for genes in self.list_of_gens:
                all_bools.append(genes.value)
                print(genes.value)
                if not genes.value:
                    print(self.ietations)
                    break
            if False not in all_bools:
                self.all_trues = True




class Dna():
    def __init__(self, chr1, chr2, chr3, chr4, chr5, chr6, chr7, chr8, chr9, chr10):
        self.list_of_chr = [chr1, chr2, chr3, chr4, chr5, chr6, chr7, chr8, chr9, chr10]
        self.chr1 = chr1
        self.chr2 = chr2
        self.chr3 = chr3
        self.chr4 = chr4
        self.chr5 = chr5
        self.chr6 = chr6
        self.chr7 = chr7
        self.chr8 = chr8
        self.chr9 = chr9
        self.chr10 = chr10
        self.mutate_ranged = 1
        self.ietations = 0
        self.all_chrom_trues = False
    def mutate(self):
        for chromosoma in self.list_of_chr:
            if random.choice([True, False]):
                chromosoma.mutate()
        # print(self.chr1_value.print_chrom())
        
# THIS IS THE PART I WAS STRUGGLING WITH< TO MAKE CHEK THE SAME FUNCTION BUT TO ALL THE CRHOMOSOMAS.
    # def all_true(self):
    #     while not self.all_chrom_trues:
    #         self.mutate()
    #         self.ietations += 1
    #         all_bools = []
    #         for chr in self.list_of_chr:
    #             print(self.ietations)
    #             chr.all_true_chrom()
    #             print(chr.list_of_gens[0])
                

                

class Organism():
    def __init__(self, dna, range_mutation):
        # self.chr1 = [dna1.chr1_value.gen1_value, dna1.chr1_value.gen2_value, dna1.chr1_value.gen3_value, dna1.chr1_value.gen4_value, dna1.chr1_value.gen5_value, dna1.chr1_value.gen6_value, dna1.chr1_value.gen7_value, dna1.chr1_value.gen8_value, dna1.chr1_value.gen9_value, dna1.chr1_value.gen10_value]
        # self.chr2 = [dna1.chr2_value.gen1_value, dna1.chr2_value.gen2_value, dna1.chr2_value.gen3_value, dna1.chr2_value.gen4_value, dna1.chr2_value.gen5_value, dna1.chr2_value.gen6_value, dna1.chr2_value.gen7_value, dna1.chr2_value.gen8_value, dna1.chr2_value.gen9_value, dna1.chr2_value.gen10_value]
        # self.chr3 = [dna1.chr3_value.gen1_value, dna1.chr3_value.gen2_value, dna1.chr3_value.gen3_value, dna1.chr3_value.gen4_value, dna1.chr3_value.gen5_value, dna1.chr3_value.gen6_value, dna1.chr3_value.gen7_value, dna1.chr3_value.gen8_value, dna1.chr3_value.gen9_value, dna1.chr3_value.gen10_value]
        # self.chr4 = [dna1.chr4_value.gen1_value, dna1.chr4_value.gen2_value, dna1.chr4_value.gen3_value, dna1.chr4_value.gen4_value, dna1.chr4_value.gen5_value, dna1.chr4_value.gen6_value, dna1.chr4_value.gen7_value, dna1.chr4_value.gen8_value, dna1.chr4_value.gen9_value, dna1.chr4_value.gen10_value]
        # self.chr5 = [dna1.chr5_value.gen1_value, dna1.chr5_value.gen2_value, dna1.chr5_value.gen3_value, dna1.chr5_value.gen4_value, dna1.chr5_value.gen5_value, dna1.chr5_value.gen6_value, dna1.chr5_value.gen7_value, dna1.chr5_value.gen8_value, dna1.chr5_value.gen9_value, dna1.chr5_value.gen10_value]
        # self.chr6 = [dna1.chr6_value.gen1_value, dna1.chr6_value.gen2_value, dna1.chr6_value.gen3_value, dna1.chr6_value.gen4_value, dna1.chr6_value.gen5_value, dna1.chr6_value.gen6_value, dna1.chr6_value.gen7_value, dna1.chr6_value.gen8_value, dna1.chr6_value.gen9_value, dna1.chr6_value.gen10_value]
        # self.chr7 = [dna1.chr7_value.gen1_value, dna1.chr7_value.gen2_value, dna1.chr7_value.gen3_value, dna1.chr7_value.gen4_value, dna1.chr7_value.gen5_value, dna1.chr7_value.gen6_value, dna1.chr7_value.gen7_value, dna1.chr7_value.gen8_value, dna1.chr7_value.gen9_value, dna1.chr7_value.gen10_value]
        # self.chr8 = [dna1.chr8_value.gen1_value, dna1.chr8_value.gen2_value, dna1.chr8_value.gen3_value, dna1.chr8_value.gen4_value, dna1.chr8_value.gen5_value, dna1.chr8_value.gen6_value, dna1.chr8_value.gen7_value, dna1.chr8_value.gen8_value, dna1.chr8_value.gen9_value, dna1.chr8_value.gen10_value]
        # self.chr9 = [dna1.chr9_value.gen1_value, dna1.chr9_value.gen2_value, dna1.chr9_value.gen3_value, dna1.chr9_value.gen4_value, dna1.chr9_value.gen5_value, dna1.chr9_value.gen6_value, dna1.chr9_value.gen7_value, dna1.chr9_value.gen8_value, dna1.chr9_value.gen9_value, dna1.chr9_value.gen10_value]
        # self.chr10 = [dna1.chr10_value.gen1_value, dna1.chr10_value.gen2_value, dna1.chr10_value.gen3_value, dna1.chr10_value.gen4_value, dna1.chr10_value.gen5_value, dna1.chr10_value.gen6_value, dna1.chr10_value.gen7_value, dna1.chr10_value.gen8_value, dna1.chr10_value.gen9_value, dna1.chr10_value.gen10_value]
        self.sistem = [dna.chr1, dna.chr2, dna.chr3, dna.chr4, dna.chr5, dna.chr6, dna.chr7, dna.chr8, dna.chr9, dna.chr10]  
        # self.complete_sistem = [self.chr1, self.chr2, self.chr3, self.chr4, self.chr5, self.chr6, self.chr7, self.chr8, self.chr9, self.chr10]
        dna.mutate_ranged = range_mutation
        self.all_1 = False
        self.iterations = 0
        self.dna = dna
        # print(self.sistem)

    def mutate(self):
        for chromosoma in self.sistem:
            if random.choice([True, False]):
                chromosoma.mutate()


    def mutate_until_all_1(self):
        while not self.all_1:
            print(self.sistem[0].gen1_value)
            self.sistem[0].gen6_value.
                        
                    
                                       
                        
                        
            # print(self.iterations)
        self.all_1 = True







gen1 = Genes()
gen2 = Genes()
gen3 = Genes()
gen4 = Genes()
gen5 = Genes()
gen6 = Genes()
gen7 = Genes()
gen8 = Genes()
gen9 = Genes()
gen10 = Genes()

gen11 = Genes()
gen12 = Genes()
gen13 = Genes()
gen14 = Genes()
gen15 = Genes()
gen16 = Genes()
gen17 = Genes()
gen18 = Genes()
gen19 = Genes()
gen20 = Genes()


gen21 = Genes()
gen22 = Genes()
gen23 = Genes()
gen24 = Genes()
gen25 = Genes()
gen26 = Genes()
gen27 = Genes()
gen28 = Genes()
gen29 = Genes()
gen30 = Genes()


gen31 = Genes()
gen32 = Genes()
gen33 = Genes()
gen34 = Genes()
gen35 = Genes()
gen36 = Genes()
gen37 = Genes()
gen38 = Genes()
gen39 = Genes()
gen40 = Genes()

gen41 = Genes()
gen42 = Genes()
gen43 = Genes()
gen44 = Genes()
gen45 = Genes()
gen46 = Genes()
gen47 = Genes()
gen48 = Genes()
gen49 = Genes()
gen50 = Genes()

gen51 = Genes()
gen52 = Genes()
gen53 = Genes()
gen54 = Genes()
gen55 = Genes()
gen56 = Genes()
gen57 = Genes()
gen58 = Genes()
gen59 = Genes()
gen60 = Genes()

gen61 = Genes()
gen62 = Genes()
gen63 = Genes()
gen64 = Genes()
gen65 = Genes()
gen66 = Genes()
gen67 = Genes()
gen68 = Genes()
gen69 = Genes()
gen70 = Genes()

gen71 = Genes()
gen72 = Genes()
gen73 = Genes()
gen74 = Genes()
gen75 = Genes()
gen76 = Genes()
gen77 = Genes()
gen78 = Genes()
gen79 = Genes()
gen80 = Genes()

gen81 = Genes()
gen82 = Genes()
gen83 = Genes()
gen84 = Genes()
gen85 = Genes()
gen86 = Genes()
gen87 = Genes()
gen88 = Genes()
gen89 = Genes()
gen90 = Genes()

gen91 = Genes()
gen92 = Genes()
gen93 = Genes()
gen94 = Genes()
gen95 = Genes()
gen96 = Genes()
gen97 = Genes()
gen98 = Genes()
gen99 = Genes()
gen100 = Genes()

print(gen1.value)
chromosome_1 = Chromosome(gen1, gen2, gen3, gen4, gen5, gen6, gen7, gen8, gen9, gen10)
chromosome_2 = Chromosome(gen11, gen12, gen13, gen14, gen15, gen16, gen17, gen18, gen19, gen20)
chromosome_3 = Chromosome(gen21, gen22, gen23, gen24, gen25, gen26, gen27, gen28, gen29, gen30)
chromosome_4 = Chromosome(gen31, gen32, gen33, gen34, gen35, gen36, gen37, gen38, gen39, gen40)
chromosome_5 = Chromosome(gen41, gen42, gen43, gen44, gen45, gen46, gen47, gen48, gen49, gen50)
chromosome_6 = Chromosome(gen51, gen2, gen3, gen4, gen5, gen6, gen57, gen58, gen59, gen60)
chromosome_7 = Chromosome(gen61, gen62, gen63, gen64, gen65, gen66, gen67, gen68, gen69, gen70)
chromosome_8 = Chromosome(gen71, gen72, gen53, gen54, gen55, gen56, gen77, gen78, gen79, gen80)
chromosome_9 = Chromosome(gen81, gen82, gen83, gen84, gen85, gen86, gen87, gen88, gen89, gen90)
chromosome_10 = Chromosome(gen91, gen92, gen93, gen94, gen95, gen96, gen97, gen98, gen99, gen100)


# chromosome_1.print_chrom()
# chromosome_2.print_chrom()
# chromosome_1.mutate()

# chromosome_1.all_true_chrom()


dna1 = Dna(chromosome_1, chromosome_2, chromosome_3, chromosome_4, chromosome_5, chromosome_6, chromosome_7, chromosome_8, chromosome_9, chromosome_10)
# dna1.mutate()
# dna1.all_true()
organism1 = Organism(dna1, 1)
organism1.mutate_until_all_1()




# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. 
# It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosome, and it can also mutate the same way Chromosomes can.
# Implement these classes as you see fit.

# Create a new class called Organism that accepts a 
# DNA object and a environement parameter that sets the probability for its DNA to mutate.
# Instantiate a number of Organims and let them mutate until one gets to a DNA is only made of 1s. 
# Then stop and record the number of generations (iterations) it took.







# until here was working just never get to be alls 1 so i will try to implement an easier way after class







# class Gen():

#     def __init__(self):
#         self.value = random.choice([True, False])

#     def mutate(self):
#         self.value = not self.value

# class Chromosome():
#     def __init__(self):
#         self.value = [Gen() for i in range(10)]
        

#     def mutate(self):
#         for gene in self.value:
#             if random.choice([True, False]):
#                 gene.mutate()

#     def print_values(self):
#         for i in range(10):
#             print(self.value[i].value)

#     def chek_all(self):
#         initial = 0
#         list1 = []
#         for i in range(10):
#             if self.value[i].value:
#                 list1.append(self.value[i].value)
#                 return True
#             else:
#                 list1.append(self.value[i].value)
#                 self.mutate()
#                 return False
#                 # return False
                
#         print(list1)
                

# class Dna():
#     def __init__(self):
#         self.value = [Chromosome() for i in range(10)]
#         self.truevalue = True
#     def mutate(self):
#         for chromosoma in self.value:
#             if random.choice([True, False]):
#                 chromosoma.mutate()

#     def __repr__(self):
#         return str(self.value)

#     def print_values(self):
#         for i in range(10):
#             print(self.value[i].print_values())
        
#     def chek_all(self):
#         loop = True
#         initial = 0
#         list_ = []
#         while self.truevalue:
#             for i in range(10):
#                 list_.append(self.value[i].chek_all())
#                 if False in list_:
#                     print("h")
#                     loop = True
#                 else: self.truevalue = False
#                 # if False in list_:
#             #     self.mutate()
#             #     initial += 1
                
#             # else:
                


                


# dna1 = Dna()

# # dna1.print_values()
# # dna1.mutate()
# dna1.chek_all()
# print("\n\n\n\n\n\n\n\n\n\n")
# # dna1.print_values()

