package aos.actividad2.inventario.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import aos.actividad2.inventario.model.Producto;

public interface ProductoRepository extends JpaRepository<Producto, Long> {
    
}
