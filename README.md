# CavityFlow.directN-S-equations
  

  lid-driven cavity is a benchmark project in fluid mechanics, and here it was solved using direct N-S equations
  
   
  ∂u/∂t + u.∂u/∂x + v.∂u/∂y = −(1/ρ).(∂p/∂x)+ν (∂2u/∂x2 + ∂2u/∂y2)                  # N-S x-Direction

  ∂v/∂t + u.∂v/∂x + v.∂v/∂y = −(1/ρ).(∂p/∂y)+ν (∂2v/∂x2 + ∂2v/∂y2)                  # N-S y-Direction

  (∂2p/∂x2 + ∂2p∂y2) = −ρ[(∂u/∂x)*(∂u/∂x) + 2.(∂u/∂y)*(∂v/∂x) + (∂v/∂y)*(∂v/∂y)]    # pressure equation derived from two above equation and        										       # Continuty equation  (∂u/∂x) + (∂v/∂y) = 0
  
  
  Spatial domain : X ∈(0,2) Y ∈(0,2)

  Initial conditions  : u,v,p = 0 in whole spatial domain;

  Boundery Conditions : u=1 at y=2 (the "lid");

                        u,v = 0 on the other boundaries;

                        ∂p/∂y = 0 at y=0 and p=0 at y=2
                        
                        ∂p/∂x = 0 at x=0,2
                        
                        
