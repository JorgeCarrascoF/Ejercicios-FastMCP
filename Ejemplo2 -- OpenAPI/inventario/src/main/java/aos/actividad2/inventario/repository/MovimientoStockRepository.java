package aos.actividad2.inventario.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import aos.actividad2.inventario.model.MovimientoStock;
import aos.actividad2.inventario.model.Producto;

public interface MovimientoStockRepository extends JpaRepository<MovimientoStock, Long> {
    List<MovimientoStock> findByProducto(Producto producto);
    
}
