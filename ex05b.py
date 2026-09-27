def find_unit_clause(clauses):
    """
    Finds a unit clause in the list of clauses.
    """
    for clause in clauses:
        if len(clause) == 1:
            return clause[0]
    return None
def simplify_clauses(clauses, literal):
    """
    Simplifies the list of clauses by setting the given literal to True.
    """
    simplified = []
    for clause in clauses:
        if literal in clause:
            continue  # Clause is satisfied
        new_clause = [l for l in clause if l != -literal]
        if not new_clause:
            return None  # Clause is unsatisfiable
        simplified.append(new_clause)
    return simplified
def dpll(clauses, assignments):
    """
    Implements the DPLL algorithm for propositional model checking.
    """
    # Unit propagation
    unit = find_unit_clause(clauses)
    while unit is not None:
        assignments.append(unit)
        clauses = simplify_clauses(clauses, unit)
        if clauses is None:
            return False,[]
        unit = find_unit_clause(clauses)

    if not clauses:
        return True, assignments  # All clauses satisfied
    # Choose a literal
    literal = clauses[0][0]
    new_clauses = simplify_clauses(clauses, literal)
    if new_clauses is not None:
         sat,res = dpll(new_clauses, assignments + [literal])
         if sat:
             return True, res
    new_clauses = simplify_clauses(clauses, -literal)
    if new_clauses is not None:
         sat, res = dpll(new_clauses, assignments + [-literal])
         if sat:
             return True, res
    return False
def main():
    # Example: (A or B) and (not A or C) and (not B or not C)
    # Represented as CNF: [[A, B], [-A, C], [-B, -C]]
    A, B, C = 1, 2, 3  # Literal encoding
    clauses = [[A, B], [-A, C], [-B, -C]]
    # Initial empty assignments
    is_sat, assignments = dpll(clauses, [])
    if is_sat:
        print("SATISFIABLE with assignments:", assignments)
    else:
        print("UNSATISFIABLE")
if __name__ == "__main__":
    main()