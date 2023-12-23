print(
    "%.2f"
    % (
        sum(
            [
                float(i) / float(2**j)
                for i, j in zip(list(range(1, 40, 2)), list(range(20)))
            ]
        )
    )
)
