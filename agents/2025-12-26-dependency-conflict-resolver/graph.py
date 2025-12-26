# graph.py

from langgraph import StateMachine


class DependencyConflictResolverFlow(StateMachine):
    def resolve(self, conflicts):
        resolution = {}
        for package, versions in conflicts.items():
            # Here, we use a simple strategy: pick the latest version as the resolution
            # More complex strategies can be implemented
            resolution[package] = sorted(versions)[-1]
        return resolution
