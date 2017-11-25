from AnnEcosystem import Anne

eco_config = {
    "ecosystem": {
      "size": [640, 480],
      "fps_cap": 60
      }
    }

# IDE level. Define IDE functions here
#   eg add_agents, configure, run, evolve etc
def __main__():
  anne = Anne(eco_config)

  # ADD IDE code here
  anne.run()

__main__()
