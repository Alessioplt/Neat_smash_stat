import random

from Game.create_all_genes import generate
from NEAT.graph.visualise_sepciation import show_repartition
from NEAT import Genome_manager

gene_manager = generate()

genome_manager = Genome_manager.GenomeManager()
for i in range(100):
    genome_manager.create_genome(gene_manager, 5)

speciation = genome_manager.new_speciation(1, 1, 0.79, 1.5)
show_repartition(speciation)

for key in speciation:
    key.score = random.randrange(-5000, 5000)
    for value in speciation[key]:
        value.score = random.randrange(-5000, 5000)
genome_manager.new_generation(gene_manager, 5)
#TODO fix speciation
speciation = genome_manager.new_speciation(1, 1, 1, 1)
show_repartition(speciation)

genome_manager.save_population('population.meow', genome_manager.generation)