from AnnEcosystem import AnnE

eco_config = {
        "size": [640, 480],
        "fps_cap": 60
        }

def __main__():
    eco = AnnE(eco_config)

    for _ in range(20):
        eco.add_agent()

    eco.run()

__main__()
