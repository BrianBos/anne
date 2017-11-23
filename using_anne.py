from AnnEcosystem import AnnE

eco_config = {
        "game": {
            "size": [640, 480],
            "fps_cap": 60
            }
        }

# IDE level. Define IDE functions here
#   eg add_agents, configure, run, evolve etc
def __main__():
    anne = AnnE(eco_config)

    # ADD IDE code here
    anne.run()

__main__()
