from AnnEcosystem import AnnE

eco_config = {
        "size": [640, 480],
        "fps_cap": 60
        }

def __main__():
    anne = AnnE(eco_config)

    for _ in range(20):
        anne.add_agent()

    anne.run()

__main__()
