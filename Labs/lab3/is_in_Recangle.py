def isPinRectangle(r, P):
    """
        r: A list of four points, each has a x- and a y- coordinate
        P: A point
    """

    areaRectangle = 0.5*abs(
        #                 y_A      y_C      x_D      x_B
                        (r[0][1]-r[2][1])*(r[3][0]-r[1][0])
        #                  y_B     y_D       x_A     x_C
                      + (r[1][1]-r[3][1])*(r[0][0]-r[2][0])
                    )

    ABP = 0.5*(
             r[0][0]*(r[1][1]-r[2][1]) # xA(yB - yC)
            +r[1][0]*(r[2][1]-r[0][1]) # xB(yC - yA)
            +r[2][0]*(r[0][1]-r[1][1]) # xC(yA - yB)
          )
    BCP = 0.5*(
             r[1][0]*(r[2][1]-r[3][1]) # xB(yC - yD)
            +r[2][0]*(r[3][1]-r[1][1]) # xC(yD - yB)
            +r[3][0]*(r[1][1]-r[2][1]) # xD(yB - yC)
          )
    CDP = 0.5*(
             r[2][0]*(r[3][1]-r[0][1]) # xC(yD - yA)
            +r[3][0]*(r[0][1]-r[2][1]) # xD(yA - yC)
            +r[0][0]*(r[2][1]-r[3][1]) # xA(yC - yD)
          )
    DAP = 0.5*(
             r[3][0]*(r[0][1]-r[1][1]) # xD(yA - yB)
            +r[0][0]*(r[1][1]-r[3][1]) # xA(yB - yD)
            +r[1][0]*(r[3][1]-r[0][1]) # xB(yD - yA)
          )
    return areaRectangle == (ABP+BCP+CDP+DAP)
