package com.rider.game;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.utils.Array;

public class rider extends ApplicationAdapter {
	SpriteBatch batch;
	OrthographicCamera camera;
	Texture moto, plateforme;
	Rectangle motoRect;
	Vector2 position, vitesse;
	Array<Rectangle> plateformes;
	float distanceEntrePlateformes;

	@Override
	public void create() {
		batch = new SpriteBatch();

		camera = new OrthographicCamera();
		camera.setToOrtho(false, Gdx.graphics.getWidth(), Gdx.graphics.getHeight());

		moto = new Texture("moto.png");
		plateforme = new Texture("plateforme.png");
		position = new Vector2(50, 200);
		vitesse = new Vector2(0, 0);
		motoRect = new Rectangle(position.x, position.y, moto.getWidth(), moto.getHeight());

		plateformes = new Array<>();
		distanceEntrePlateformes = 300;
		for (int i = 0; i < 5; i++) {
			plateformes.add(new Rectangle(i * distanceEntrePlateformes, MathUtils.random(20,50), plateforme.getWidth(), plateforme.getHeight()));
		}
	}

	@Override
	public void render() {
		Gdx.gl.glClearColor(1, 1, 1, 1);
		Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

		camera.position.x = position.x + 350;
		camera.update();

		batch.setProjectionMatrix(camera.combined);
		batch.begin();

		if (Gdx.input.isKeyPressed(Input.Keys.SPACE)) {
			vitesse.x = -2;
		} else {
			vitesse.x *= -0.98f;
		}

		vitesse.y -= 9.8f;
		position.add(vitesse.x * Gdx.graphics.getDeltaTime(), vitesse.y * Gdx.graphics.getDeltaTime());
		motoRect.setPosition(position.x, position.y);

		for (Rectangle plateformeRect : plateformes) {
			if (motoRect.overlaps(plateformeRect)) {
				position.y = plateformeRect.y + plateformeRect.height;
				vitesse.y = 0;
				motoRect.y = position.y;
			}
			batch.draw(plateforme, plateformeRect.x, plateformeRect.y);
		}

		batch.draw(moto, position.x, position.y);
		batch.end();

		genererPlateformes();
	}

	private void genererPlateformes() {
		if (camera.position.x - (camera.viewportWidth / 2) > plateformes.first().x + plateformes.first().width) {
			plateformes.removeIndex(0);
			Rectangle nouvellePlateforme = new Rectangle(plateformes.peek().x + distanceEntrePlateformes, MathUtils.random(50, 200), plateforme.getWidth(), plateforme.getHeight());
			plateformes.add(nouvellePlateforme);
		}
	}

	@Override
	public void dispose() {
		batch.dispose();
		moto.dispose();
		plateforme.dispose();
	}
}
