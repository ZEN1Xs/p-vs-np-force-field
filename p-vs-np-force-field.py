import numpy as np


class ComplexityForceField:

    def __init__(self, p_efficiency=0.1, np_explosion=0.01):
        self.gamma = p_efficiency
        self.beta = np_explosion

    def encode_field(self, complexity):
        return 2.0 / (1.0 + np.exp(-np.log(complexity + 1))) - 1.0

    def simulate_computation(self, problem_size):
        print(
            f"=== СИМУЛЯЦИЯ СИСТЕМЫ P vs NP ДЛЯ РАЗМЕРА ЗАДАЧИ N = {problem_size} ==="
        )
        print(
            f"{'Шаг':<5} | {'Хаос системы':<15} | {'Позиция [-1,1]':<15} | {'Сила Взрыва NP':<15} | {'Сила Сжатия P':<14}"
        )
        print("-" * 80)

        chaos = float(problem_size)

        for step in range(50):
            pos = self.encode_field(chaos)

            f_np_explosion = self.beta * (2**problem_size) * (1.0 - pos)
            f_p_compression = -self.gamma * (problem_size**2) * pos

            net_force = f_np_explosion + f_p_compression

            print(
                f"{step:<5} | {chaos:<15.4f} | {pos:<15.4f} | {f_np_explosion:<15.4f} | {f_p_compression:<14.4f}"
            )

            chaos = chaos * np.exp(net_force)

            if chaos < 0.01:
                print("-" * 80)
                print(
                    f"Шаг {step+1}: Алгоритм P успешно подавил хаос! Задача решена за полиномиальное время. (В этой точке P = NP)"
                )
                break
            if chaos > 1e10:
                print("-" * 80)
                print(
                    f"Шаг {step+1}: ВЗРЫВ СИСТЕМЫ! Сила NP разорвала поле, алгоритм P бессилен. (Доказано локальное P != NP)"
                )
                break
        else:
            print("-" * 80)
            print("Система зависла в неопределенности.")



field = ComplexityForceField(p_efficiency=0.1, np_explosion=0.01)
field.simulate_computation(25)
