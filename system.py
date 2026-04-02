from amak import MAS, ExecutionPolicy

from entities import Fork, PhilosopherAgent


class PhilosophersDinnerMAS(MAS):
    def __init__(self, environment, results):
        super().__init__(environment, execution_policy=ExecutionPolicy.TWO_PHASES)
        self.cycles_count = 0
        self.results = results

        for i in range(len(environment.forks)):
            PhilosopherAgent("Philosopher "+str(i), self, environment.forks[i], environment.forks[(i + 1) % len(environment.forks)])

        for i in range(len(self.agents_pending_addition)):
            self.agents_pending_addition[i].left_neighbor = self.agents_pending_addition[(i - 1) % len(self.agents_pending_addition)]
            self.agents_pending_addition[i].right_neighbor = self.agents_pending_addition[(i + 1) % len(self.agents_pending_addition)]

    def on_system_cycle_start(self):
        self.cycles_count = self.cycles_count + 1

    def on_system_cycle_end(self):
        # ate_pastas = [agent.ate_pasta for agent in self.agents]
        ate_pastas = {

        }
        for agent in self.agents:
            ate_pastas[agent.id] = agent.ate_pasta
        self.results.append(ate_pastas)

    def is_ready_to_stop(self):
        return self.cycles_count == 100


class Table:
    def __init__(self, fork_count):
        self.forks = [Fork() for _ in range(fork_count)]

    def cycle(self):
        pass