library(igraph)

data <- read.csv('affiliations.csv', header=F)

g <- graph.data.frame(data, directed=FALSE)

bipartite.mapping(g)

V(g)$type <- bipartite_mapping(g)$type

# V(g)$color <- ifelse(V(g)$type, "lightblue", "salmon")
# V(g)$shape <- ifelse(V(g)$type, "circle", "square")
# E(g)$color <- "lightgray"
# V(g)$frame.color <-  "gray"


V(g)$shape <- ifelse(V(g)$type, "circle", "square")
V(g)$color <- ifelse(V(g)$type, "lightblue", "salmon")
V(g)$label <- NA
V(g)$size <- ifelse(V(g)$type, 5, 0.5)
E(g)$size <- .001
E(g)$color <- 'salmon'

png('bimodal_graph.png', width = 8, height = 8, units = 'in', res = 300)
plot(g, layout=layout.bipartite)
dev.off()

bipartite_matrix <- as_incidence_matrix(g)
t(bipartite_matrix)

person_matrix_prod <- bipartite_matrix %*% t(bipartite_matrix)
diag(person_matrix_prod) <- 0

g_users <- graph_from_incidence_matrix(person_matrix_prod)
V(g_users)$color <- 'lightblue'
V(g_users)$size <- 2
V(g_users)$shape <- 'circle'
V(g_users)$label <- NA
E(g_users)$size <- .001
E(g_users)$color <- 'salmon'

png('unimodal_graph.png', width = 8, height = 8, units = 'in', res = 300)
plot(g_users, layout = layout_with_fr)
dev.off()
