def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models has been printed:")
    for completed_model in completed_models:
        print("\t" + completed_model.title())


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_model(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)